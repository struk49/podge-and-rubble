from django.contrib import admin
from .models import (
    Product, MasterCategory, SpecialOffer
)


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'sku',
                ('name', 'product_description'),
                ('price', 'discount_price'),
                'image')
        }),
        ('Category Selections', {
            'classes': ('collapse',),
            'fields': (
                'gender',
                'master_category',
                'sub_category',
                'article_type',
                'special_offer'),
        }),
    )