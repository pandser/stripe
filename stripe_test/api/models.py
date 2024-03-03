from django.db import models


class Item(models.Model):
    '''Модель Item.'''
    name = models.CharField(
        max_length = 200,
        verbose_name = 'Имя',
    )
    description = models.TextField(
        verbose_name = 'Описание',
    )
    price = models.IntegerField(
        verbose_name = 'Цена',
    )
