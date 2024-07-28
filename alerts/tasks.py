from django.core.mail import send_mail
from django.conf import settings
from .models import Alert

def send_alert_email(alert_id):
    alert = Alert.objects.get(id=alert_id)
    send_mail(
        'Price Alert Triggered',
        f'The price of {alert.cryptocurrency} has reached {alert.target_price}.',
        settings.DEFAULT_FROM_EMAIL,
        [alert.user.email],
        fail_silently=False,
    )
