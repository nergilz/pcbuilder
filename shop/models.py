from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True, verbose_name='Наименование товара')
    product_type = models.CharField(max_length=100, verbose_name='Тип')
    product_image = models.ImageField(upload_to='static/images_product', verbose_name='Фото') 
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    product_quantity = models.IntegerField(verbose_name='Количество на складе')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    description = models.TextField(max_length=2000, verbose_name='Описание')

    def __str__(self):
            return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# type : cpu ram mb comp vc