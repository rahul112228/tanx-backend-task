import asyncio
import json
import logging
from django.core.management.base import BaseCommand
import websockets
from alerts.models import Alert
from alerts.tasks import send_alert_email

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Connects to Binance WebSocket and processes price updates.'

    async def price_update(self):
        uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
        async with websockets.connect(uri) as websocket:
            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)
                    current_price = float(data['p'])
                    logger.info(f"Current BTC price: ${current_price}")
                    alerts = Alert.objects.filter(cryptocurrency='BTC', target_price__lte=current_price, status='created')
                    for alert in alerts:
                        alert.status = 'triggered'
                        alert.save()
                        send_alert_email(alert.id)

                except Exception as e:
                    logger.error(f"Error processing WebSocket data: {e}")

    def handle(self, *args, **kwargs):
        asyncio.run(self.price_update())
