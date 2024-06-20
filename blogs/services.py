from django.core.cache import cache

from blogs.models import Blog
from config.settings import CASH_ENABLED


def get_blogs_from_cache():
    """Получает данные по статьям из кэша, если кэш пуст, получает из бд"""
    if not CASH_ENABLED:
        return Blog.objects.all()
    key = 'blogs_list'
    blogs = cache.get(key)
    if blogs is not None:
        return blogs
    blogs = Blog.objects.all()
    cache.set(key, blogs)
    return blogs
