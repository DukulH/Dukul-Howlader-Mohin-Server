from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField (primary_key=True)
    customer_name = models.CharField(max_length=255, null=False)
    customer_email = models.EmailField(max_length=255, null=False)
    customer_contact = models.IntegerField(null=False)
    customer_address = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-customer_id']
        db_table = 'Customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255, null=False)
    category_description = models.CharField(max_length=255, null=True)
    
    class Meta:
        ordering = ['-category_id']
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
        
class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=255, null=False)
    region_name = models.CharField(max_length=255, null=False)
    post_code = models.IntegerField(default=0, null=False)
    
    class Meta:
        ordering = ['-region_id']
        db_table = 'Region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        
        
class Product(models.Model):
    product_id = models.IntegerField (primary_key=True)
    category= models.ForeignKey(Category, related_name="categories", on_delete=models.PROTECT)
    product_name = models.CharField(max_length=255, null=False)
    product_description = models.EmailField(max_length=255, null=False)
    product_price = models.IntegerField(null=False)
    product_stock = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-product_id']
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
class Order (models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateField(max_length=255, null=False)
    order_total = models.IntegerField(default=0, null=False)
    customer = models.ForeignKey(Customer, related_name="customers", on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['-order_id']
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
        
class Order_Details(models.Model):
    order_details_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, related_name='orders', on_delete=models.PROTECT )
    product = models.ForeignKey(Product, related_name='products', on_delete=models.PROTECT)
    region = models.ForeignKey(Region, related_name='regions', on_delete=models.PROTECT)
    product_quantity = models.IntegerField(default=1, null=False)
    product_price = models.IntegerField(default=0, null=False)
    sub_total = models.IntegerField( default=0, null=False)
    
    class Meta:
        ordering = ['-order_details_id']
        db_table = 'Order_Details'
        verbose_name = 'Order_Details'