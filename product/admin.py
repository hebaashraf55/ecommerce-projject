from itertools import product
from django.contrib import admin
from .models import Product , ProductImage ,Category, ProductAlternative, Product_Accessories

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductAlternative)
admin.site.register(Product_Accessories)
