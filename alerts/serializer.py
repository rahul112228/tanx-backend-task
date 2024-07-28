from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)

    class Meta:
        model = Alert
        fields = ['username', 'cryptocurrency', 'target_price', 'status']

    def create(self, validated_data):
        username = validated_data.pop('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError(f"User with username '{username}' does not exist.")
        alert = Alert.objects.create(user=user, **validated_data)
        return alert

