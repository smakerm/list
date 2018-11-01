from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age' ,'email']
    list_display_links = ('name', 'email')
    list_editable = ('age',)
    search_fields = ('name','email')
    list_filter = ('name',)
    # fields = ('name', 'age', 'email', 'picture')
    fieldsets = (
        ('基本信息',{'fields':('name','age','publisher')}),
        ('高级设置',{'fields':('email', 'picture'),'classes':('collapse',)})
        )

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publication_date','publisher')
    date_hierarchy = 'publication_date'

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
    list_editable = ('address', 'city')
    list_display_links = ('name',)
    list_filter = ('address', 'city')
    fieldsets = (
        ('基本选项',{'fields':('name', 'address','city',)}),
        ('可选选项',{'fields':('country','website'),'classes':('collapse',)})
    )

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)