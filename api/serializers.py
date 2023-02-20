from rest_framework import serializers
from .models import Product, Order, Order_Details, Category, Region, Customer

class ProductSerializer(serializers.ModelSerializer):
        quantity = serializers.SerializerMethodField()
        category_id = serializers.SerializerMethodField()
        category_name = serializers.SerializerMethodField()
        total_sale_price = serializers.SerializerMethodField()
        
        class Meta:
            model = Product
            fields = "__all__"
        def get_quantity(self,obj):
            if(obj.quantity):
                return obj.quantity
            else:
                return ''
        def get_category_id(self,obj):
            if(obj.category_id):
                return obj.category_id
            else:
                return ''
        def get_category_name(self,obj):
            if(obj.category_name):
                return obj.category_name
            else:
                return ''
        def get_total_sale_price(self,obj):
            if hasattr(obj, 'total_sale_price'):
                return obj.total_sale_price
            else:
                return ''
            
class OrderSerializer(serializers.ModelSerializer):
        region_id = serializers.SerializerMethodField()
        class Meta:
            model = Order
            fields = "__all__"
            
        def get_region_id(self, obj):
            if hasattr(obj, 'region_id'):
                return obj.region_id
            else:
                return ""
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
    
        order_total_amount =serializers.SerializerMethodField()
        class Meta:
            model = Customer
            fields = "__all__"
        def get_order_total_amount(self,obj):
            if hasattr(obj, 'order_total_amount'):
                return obj.order_total_amount
            else:
                return ''