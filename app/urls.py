from django.urls import path, include
from django.views.generic import RedirectView

from .views import RegistrationView, LoginView, LogoutView
urlpatterns = [
    path("registration/", RegistrationView.as_view(), name='registration'),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('drf-auth/', include('rest_framework.urls'))
]
