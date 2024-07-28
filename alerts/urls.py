from django.urls import path
from .views import CreateAlertView, DeleteAlertView, ListAlertsView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('alerts/create/', CreateAlertView.as_view(), name='create-alert'),
    path('alerts/delete/<str:username>/<str:cryptocurrency>/', DeleteAlertView.as_view(), name='delete-alert'),
    path('alerts/', ListAlertsView.as_view(), name='list-alerts'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

