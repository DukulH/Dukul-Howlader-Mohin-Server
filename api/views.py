
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Order_Details, Order, Region
from django.db.models import Sum, Count

@api_view(['GET'])
def getCardData(request):
    total_sales = Order.objects.aggregate(Sum('order_total'))
    total_stores = Region.objects.aggregate(Count('region_id'))
    total_orders = Order.objects.aggregate(Count('order_id'))
    total_products = Product.objects.aggregate(Count('product_id'))
    return_data={}
    return_data.update(total_sales),
    return_data.update(total_stores),
    return_data.update(total_products),
    return_data.update(total_orders),
    return Response(return_data)