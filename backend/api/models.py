from django.db import models


class WHThings(models.Model):
    brand = models.CharField(
        max_length=255,
        verbose_name='Бренд',
        null=True,
        blank=True)
    color = models.CharField(
        max_length=100,
        verbose_name='Цвет',
        null=True,
        blank=True)
    entity = models.CharField(
        max_length=100,
        verbose_name='Сущность',
        null=True,
        blank=True)
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        null=True,
        blank=True)
    review_rating = models.FloatField(
        verbose_name='Рейтинг отзывов',
        null=True,
        blank=True)
    supplier = models.CharField(
        max_length=255,
        verbose_name='Поставщик',
        null=True, blank=True)
    supplier_id = models.CharField(
        max_length=255,
        verbose_name='ID поставщика',
        null=True,
        blank=True)
    supplier_rating = models.FloatField(
        verbose_name='Рейтинг поставщика',
        null=True,
        blank=True)
    product_id = models.CharField(
        max_length=255,
        verbose_name='ID товара',
        unique=True)
    price_basic = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Базовая цена',
        null=True,
        blank=True)

    qty = models.IntegerField(
        verbose_name='Доступно на складе',
        null=True,
        blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.created_at}'
