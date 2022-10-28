from django.urls import path
from knox import views as knox_views

from authentication.views import (
    LoginAPIView,
    OAuthAPIView,
    RegisterAPIView,
    VerificationAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("verify/", VerificationAPIView.as_view(), name="verify"),
    path("oauth/", OAuthAPIView.as_view(), name="oauth"),
]