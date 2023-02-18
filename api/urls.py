from django.urls import path 
from . import views

urlpatterns = [
    path('cardData', views.getCardData),
]