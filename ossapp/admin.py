from django.contrib import admin
from . models import Login, Customer, Product, Category
#class AdminProduct(admin.ModelAdmin):
#    list_display= ['name','price','desc','category']

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','desc','image']
class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Login)
admin.site.register(Customer)
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)