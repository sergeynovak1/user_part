from django.urls import path
from django.views.generic import RedirectView

from .views import login_view, logout_view, RegistrationView
urlpatterns = [
    path("registration/", RegistrationView.as_view(), name='registration'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]
