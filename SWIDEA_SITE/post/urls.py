from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', ideaManage , name='ideaManage'),
    path('idea/Register/',ideaRegister , name="ideaRegister"),
    path('idea/detail/<int:pk>/',ideaDetail , name="ideaDetail"),
    path('idea/delete/<int:pk>/' , ideaDelete , name="ideaDelete"),
    path('idea/update/<int:pk>/' , ideaUpdate , name='ideaUpdate'),
    path('post/<int:pk>/toggle_star/', toggle_star, name='toggle_star'), 
    path('post/<int:pk>/plusInterest/' , plusInterest , name="plusInterest"),
    path('post/<int:pk>/minusInterest/' , minusInterest , name="minusInterest"),
]