from django.contrib import admin
from .models import Product,Search_history,Cart

# Register your models here.
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','p_name','p_price','p_disc','p_specification']

@admin.register(Search_history)
class SearchAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','item','data','searched_on']

@admin.register(Cart)
class SearchAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','item','quantity']



