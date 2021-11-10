from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
 
class Categories(models.Model):
    menu_id  = models.ForeignKey('Menu', on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
 
class Products(models.Model):
    category_id = models.ForeignKey('Categories', on_delete = models.CASCADE)
    kr_name = models.CharField(max_length = 20)
    en_name = models.CharField(max_length = 20)
    product_info = models.TextField()
    new_product = models.BooleanField()
    
    def __str__(self):
        return self.kr_name
 
class Nutritions(models.Model):
    product_id = models.ForeignKey('Products', on_delete = models.CASCADE)
    calories = models.IntegerField(default = 0)
    total_Fat = models.IntegerField(default = 0)
    sodium = models.IntegerField(default = 0) 
    total_Carbohydrates = models.FloatField(default = 0)
    protein = models.IntegerField(default = 0)
    caffeine = models.IntegerField(default = 0)

class Allergies(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
 
class Product_allergies(models.Model):
    product_id = models.ForeignKey('Products',on_delete = models.CASCADE)
    allergy_id = models.ForeignKey('Allergies', on_delete = models.CASCADE)
