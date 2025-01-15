from django.urls import path
from .views import *

app_name='DevTool'

urlpatterns = [
    path('tool/Manage' , toolManage , name="toolManage"),
    path('tool/detail/<int:pk>' , toolDetail , name="toolDetail"),
    path('tool/register' , toolRegister , name="toolRegister"),
    path('tool/delete/<int:pk>',toolDelete , name="toolDelete"),
    path('tool/update/<int:pk>',toolUpdate , name="toolUpdate"),
]
