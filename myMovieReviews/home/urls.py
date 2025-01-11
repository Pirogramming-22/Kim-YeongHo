from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('add/' , add , name="add"),
    path('detail/<int:pk>/', detail , name="detail"),
    path('delete/<int:pk>/' , delete , name="delete"),
    path('edit/<int:pk>/' , edit , name="edit"),
]