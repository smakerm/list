from django.contrib import admin
from .models import *
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    fields = ('uphone','uemail','uname','isActive')
    search_fields = ('uphone','uemail','uname')

admin.site.register(Users,UsersAdmin)
admin.site.register(GoodsType)
admin.site.register(Goods)
