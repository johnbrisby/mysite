from django.contrib import admin

from .models import Category,Item,Doctype

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Doctype)
