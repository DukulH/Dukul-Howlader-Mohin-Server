from django.urls import path 
from . import views

urlpatterns = [
    path('cardData/', views.getCardData),
    path('categoryWiseData/<int:id>/', views.getCategoryWiseTopSellingProductData),
    path('topProductData/', views.getTopProductsData),
    path('topCustomerData/', views.getTopCustomerData),
]