from django.urls import path
from . import views
from .views import signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup")
]