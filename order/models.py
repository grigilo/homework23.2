from django.db import models


class Order(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE,
                                verbose_name='Продукт')

    name = models.CharField(max_length=50, verbose_name='Имя')
    message = models.TextField(verbose_name='Сообщение')
    email = models.EmailField(max_length=50, verbose_name='Email')
    closed = models.BooleanField(default=False, verbose_name='Закрыто')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} от {self.name}({self.email})'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
