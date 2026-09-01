from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
    path('novo/', views.criar_pessoa, name='criar_pessoa'),
]