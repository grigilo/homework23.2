from django.core.mail import send_mail

from catalog.models import Product
from config import settings


def send_order_email(order_item):
    send_mail(
        'Заявка на покупку продукта',
        f'{order_item.name} ({order_item.email}) заказал продукт {order_item.product.name} стоимостью {order_item.product.price}. Сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.email]
    )


def send_max_count_email(data):
    send_mail(
        'Уведомление',
        f'Просмотр вашей публикации "{data.title}" достиг 15',
        settings.EMAIL_HOST_USER,
        ['tsoy@cosmopharm.ru']
    )
