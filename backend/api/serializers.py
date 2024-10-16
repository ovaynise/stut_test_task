from rest_framework import serializers
from .models import WHThings


class WHThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WHThings
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'Бренд': representation['brand'],
            'Цвет': representation['color'],
            'Сущность': representation['entity'],
            'Название': representation['name'],
            'Рейтинг отзывов': representation['review_rating'],
            'Поставщик': representation['supplier'],
            'ID поставщика': representation['supplier_id'],
            'Рейтинг поставщика': representation['supplier_rating'],
            'ID товара': representation['product_id'],
            'Базовая цена': representation['price_basic'],
            'Доступно на складе': representation['qty'],
            'Дата создания': representation['created_at'],
        }
