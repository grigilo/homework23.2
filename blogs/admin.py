from django.contrib import admin

from blogs.models import Blog, Release


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = (
    'pk', 'blog', 'release_number', 'release_title', 'activated')
    list_filter = ('activated',)
    search_fields = ('release_title',)
