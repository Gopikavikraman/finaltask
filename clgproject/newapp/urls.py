from . import views
from django.urls import path
from .views import register,user_login,user_logout
# app_name='newapp'
urlpatterns = [

    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('buttonpage',views.buttonpage, name='buttonpage'),
    path('order',views.order, name='order')
]