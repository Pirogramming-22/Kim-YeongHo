from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
    path('comment_register/', views.comment_register, name='comment_register'),
    path('comment_delete/', views.comment_delete, name='comment_delete'),
]