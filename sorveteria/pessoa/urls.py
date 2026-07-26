from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Funciona em http://127.0.0.1:8000/
    path('index/', views.home, name='index'),   # Funciona em http://127.0.0.1:8000/index/
    path('about/', views.about, name='about'),
    path('icecream/', views.icecream, name='icecream'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]