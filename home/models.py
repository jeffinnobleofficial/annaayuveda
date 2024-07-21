
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    pro_name = models.CharField(max_length=100)
    pro_price = models.CharField(max_length=10)
    pro_quantity = models.CharField(max_length=5)
    pro_image = models.ImageField(upload_to='products')
    
    def __str__(self):
        return self.pro_name
    
class shop(models.Model):
    sname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    
class appointments(models.Model):
    doct_name = models.CharField(max_length=100)
    doc_spec = models.TextField()
    date = models.DateField()
    

    
    
    
    

