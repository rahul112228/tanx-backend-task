from django.shortcuts import render
from rest_framework import generics, status,permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Alert
from .serializer import AlertSerializer
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User

class CreateAlertView(generics.CreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

class DeleteAlertView(generics.UpdateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        cryptocurrency = self.kwargs.get('cryptocurrency')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound(f"User with username '{username}' does not exist.")
        
        return Alert.objects.filter(user=user, cryptocurrency=cryptocurrency).exclude(status='deleted')

    def update(self, request, *args, **kwargs):
        alerts = self.get_queryset()
        if not alerts.exists():
            return Response({"detail": "No alerts found to update."}, status=status.HTTP_404_NOT_FOUND)

        alerts.update(status='deleted')
        return Response({"detail": "Alerts status changed to deleted."}, status=status.HTTP_200_OK)
    
class ListAlertsView(generics.ListAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status_filter = self.request.query_params.get('status', None)
        queryset = Alert.objects.filter(user=user)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset
