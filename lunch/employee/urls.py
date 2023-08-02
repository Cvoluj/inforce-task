from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, AuthUserAPIView


urlpatterns = [
      path('api/register/', RegisterAPIView.as_view(), name='register'),
      path('api/login/', LoginAPIView.as_view(), name="login"),
      path('api/user/', AuthUserAPIView.as_view(), name="user")
]