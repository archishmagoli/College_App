from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="contacts"),
    path('update_contact/<str:pk>/', views.updateContact, name="update_contact"),
    path('remove_contact/<str:pk>/', views.removeContact, name="remove_contact"),

]
