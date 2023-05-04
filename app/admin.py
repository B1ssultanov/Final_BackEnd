from django.contrib import admin
from app.models import Products, Categories


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


# Login: b1ssultanov
# Password: b1ssultanov
