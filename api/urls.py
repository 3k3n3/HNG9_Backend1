from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.getProfile, name='getProfile'), # Task1
    path("calculate/", views.calculate, name="calc"), # Task2
]