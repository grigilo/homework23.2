from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/photo/', **NULLABLE,
                              verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    count = models.IntegerField(default=0, verbose_name='Количество')
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True,
                                  verbose_name='Дата последнего изменения')

    # manufactured_at = models.DateField(**NULLABLE,
    #                                    verbose_name="Дата производства")

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
