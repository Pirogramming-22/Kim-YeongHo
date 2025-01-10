from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('add/' , add , name="add"),
    path('detail/', detail , name="detail"),
    
]