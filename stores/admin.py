from django.contrib import admin
from .models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display=('id' ,'name' ,'slug' ,'description',)
    list_editable = ('description',)
admin.site.register(Store, StoreAdmin)
