from django.contrib import admin

from django.contrib import admin
from accounts.models import MyUser

class MyuserAdmin(admin.ModelAdmin):
    
    list_display = ('username',)
    search_fields = ('username',)
    
admin.site.register(MyUser,MyuserAdmin)
    
# Register your models here.

