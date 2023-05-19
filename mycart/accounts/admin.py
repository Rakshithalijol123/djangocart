from django.contrib import admin
from .models import Registration

# Register your models here.

# admin.site.register(Registration)
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','user','no']
