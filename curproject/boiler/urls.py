from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('goods/', views.goods, name = 'goods'),

    path('contact/', views.contact, name = 'contact'),

    path('info/', views.info, name = 'info')

]