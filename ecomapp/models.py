from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.CharField(max_length=500)

    def __str__(self):
        return self.productname
    

class Product_Detail(models.Model):
    pid=models.ForeignKey(Product,models.CASCADE)
    caty=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    image=models.CharField(max_length=500)

    def __str__(self):
        return self.caty

class Brand_Detail(models.Model):
    pid=models.ForeignKey(Product_Detail,models.CASCADE)
    brandname=models.CharField(max_length=50)
    image=models.CharField(max_length=500)
    avgprice=models.IntegerField(max_length=15)

    def __str__(self):
        return self.brandname
    
class Final_Detail(models.Model):
    cid=models.ForeignKey(Brand_Detail,models.CASCADE)
    specify=models.CharField(max_length=200)
    brand=models.CharField(max_length=50)
    price=models.IntegerField(max_length=15)
    image=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.specify

class Conclude_Detail(models.Model):
    kid=models.ForeignKey(Final_Detail,models.CASCADE)
    text_specify=models.CharField(max_length=200)
    pro_brand=models.CharField(max_length=50)
    price=models.IntegerField(max_length=15)
    image=models.CharField(max_length=500, default="")
    status=models.BooleanField(default=True)
    color=models.CharField(max_length=20)


    def __str__(self):
        return self.text_specify