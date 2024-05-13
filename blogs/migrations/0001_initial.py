# Generated by Django 5.0.4 on 2024-05-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='загаловок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/photo/', verbose_name='изображение')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликован')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
