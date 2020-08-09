from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=80)
    product_description = models.CharField(max_length=200)
    product_price=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    publishing_date = models.DateField()
    product_image=models.ImageField(default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=80,default="")
    phone =models.CharField(max_length=13,default="")
    description =models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=100000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress= models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    district =models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode=models.CharField(max_length=20)
    phone =models.CharField(max_length=13,default="")
   

class track(models.Model):
    updateid=models.AutoField(primary_key=True)
    orderid=models.IntegerField(default="")
    updatedesc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.updatedesc[0:10]+"...."