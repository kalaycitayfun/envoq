from django.db import models

# Create your models here.

class Product(models.Model):
    
    title = models.CharField(max_length=255)
    
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    description = models.TextField(black=True)
    
    slug =  models.SlugField(max_length=255)
    
    brand = models.CharField(max_length=255,default='un-brand')
    
    image = models.ImageField(upload_to = 'images/')


    class Meta:
        
        verbose_name_plural = 'Products'
        
    
    def __str__(self):
        
        return self.title


class Category(models.Model):
    
        name = models.CharField(max_length=255, db_index=)
    
    
    
    
    
    
    
    
    