from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("login", views.login, name="login"), 
    path("health", views.health, name="health"),
    path("calendar", views.calendar, name="calendar"),
    path("checklist", views.checklist, name="checklist"),
    path("contacts", views.contacts, name="contacts"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("financial_aid", views.financial_aid, name="financial_aid"),
    path("search", views.search, name="search"),
    path("my_colleges", views.my_colleges, name="my_colleges"),
    path("news", views.news, name="News"),
    path("path2college", views.path2college, name="path2college")
]