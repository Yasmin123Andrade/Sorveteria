from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('novo/', views.criar_pedido, name='criar_pedido'),
]