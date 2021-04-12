from django.urls import path
from . import views

urlpatterns = [
    path("health", views.health, name="health"),
    path("checklist", views.checklist, name="checklist"),
    path("contacts", views.contacts, name="contacts"),
    path("financial_aid", views.financial_aid, name="financial_aid"),
    path("search", views.search, name="search"),
    path("my_colleges", views.my_colleges, name="my_colleges"),
    path("news", views.news, name="news"),
    path("path2college", views.path2college, name="path2college")
]