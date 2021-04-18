from django.urls import path
from . import views

urlpatterns = [
    path("health", views.health, name="health"),
    path("financial_aid", views.financial_aid, name="financial_aid"),
    path("search", views.search, name="search"),
    path("news", views.news, name="news"),
    path("path2college", views.path2college, name="path2college")
]