from django.contrib import admin

from .models import WHThings


class WHThingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'color',
        'entity',
        'name',
        'review_rating',
        'supplier',
        'supplier_id',
        'supplier_rating',
        'product_id',
        'price_basic',
        'qty',
        'created_at'
    )
    empty_value_display = 'Не задано'


admin.site.register(WHThings, WHThingsAdmin)

