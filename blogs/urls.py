from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogCreateView

app_name = BlogsConfig.name


urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    # path(' ', ..., name='list'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),
]
