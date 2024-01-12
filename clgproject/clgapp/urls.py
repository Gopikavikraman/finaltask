from django.urls import path
from . import views

from django.conf.urls.static import static
app_name='clgapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('buttonpage', views.buttonpage, name='buttonpage'),
    path('newpage', views.newpage, name='newpage'),
    path('order', views.order, name='order'),


]