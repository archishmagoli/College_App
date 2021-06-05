from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mycolleges"),
    path('update_college/<str:pk>/', views.updateCollege, name="update_college"),
    path('remove_college/<str:pk>/', views.removeCollege, name="remove_college")

]