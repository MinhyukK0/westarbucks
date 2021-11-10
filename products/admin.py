from django.contrib import admin

# Register your models here.

from .models import Menu, Categories, Products, Nutritions, Allergies, Product_allergies

admin.site.register(Menu)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Nutritions)
admin.site.register(Allergies)
admin.site.register(Product_allergies)