from django.db import models

from catalog.models import NULLABLE
from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='загаловок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое')
    image = models.ImageField(upload_to='products/photo/', **NULLABLE,
                              verbose_name='изображение')
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name='дата создания')

    is_published = models.BooleanField(default=True,
                                       verbose_name='опубликован')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    author = models.ForeignKey(User, verbose_name="автор", **NULLABLE,
                               on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Release(models.Model):
    blog = models.ForeignKey(Blog, related_name="releases",
                             on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='блог')

    release_number = models.CharField(max_length=100, null=True,
                                      blank=True,
                                      verbose_name='номер релиза')
    release_title = models.CharField(max_length=100, null=True,
                                     blank=True,
                                     verbose_name='название релиза')
    release_content = models.TextField(null=True,
                                       blank=True, verbose_name='содержимое')
    activated = models.BooleanField(default=True, verbose_name='активен')

    def __str__(self):
        return f'{self.release_title}'

    class Meta:
        verbose_name = 'Релиз'
        verbose_name_plural = 'Релизы'
