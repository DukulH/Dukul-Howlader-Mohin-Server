from rest_framework import serializers
from .models import Product, Order, Order_Details, Category, Region, Customer

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = "__all__"
            
class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = "__all__"
            
            
class OrderDetailsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order_Details
            fields = "__all__"
            
            
class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = "__all__"
            
            
class RegionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Region
            fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Customer
            fields = "__all__"