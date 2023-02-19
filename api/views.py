
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Order, Region, Customer
from django.db.models import Sum, Count
from .serializers import ProductSerializer, CustomerSerializer

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

@api_view(['GET'])
def getCategoryWiseTopSellingProductData(request, *args, **kwargs):
    category_id = kwargs['id']
    categoryWiseData = Product.objects.raw('''
            Select * from (select p.product_id,od.quantity,p.product_name, c.category_id, c.category_name
            from
            public."Product" as p, 
            public."Category" as c,
            (select product_id ,count(*) as quantity from public."Order_Details" group by product_id) as od
            where p.product_id = od.product_id and p.category_id = c.category_id) as X
            where X.category_id = %s
            
            ''',[category_id])
    data = ProductSerializer(categoryWiseData, many=True).data
    return Response(data)

@api_view(["GET"])
def getTopProductsData(request):
    topProductData = Product.objects.raw('''
    SELECT * FROM (select p.product_id,od.quantity,p.product_name, (p.product_price * od.quantity) as total_sale_price, c.category_name
    from  public."Product" as p, public."Category" as c,
    (select product_id ,count(*) as quantity from public."Order_Details" group by product_id) as od
    where p.category_id = c.category_id and p.product_id = od.product_id) as X
    order by quantity desc
    LIMIT 5
    ''')
    data = ProductSerializer(topProductData, many=True).data
    return Response(data)

@api_view(["GET"])
def getTopCustomerData(request):
    topCustomerData = Customer.objects.raw('''
        select o.customer_id, c.customer_name, sum(order_total) as order_total_amount 
        from public."Order" as o, public."Customer" as c 
        where o.customer_id = c.customer_id
        group by o.customer_id,c.customer_name
        order by sum(order_total) desc
        Limit 3
    ''')
    data = CustomerSerializer(topCustomerData, many=True).data
    return Response(data)