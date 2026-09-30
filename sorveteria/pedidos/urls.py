from django.urls import path

from . import views


urlpatterns = [

    path('', views.listar_pedidos, name='lista_pedidos'),

    path('novo/', views.criar_pedido, name='criar_pedido'),

    path('<int:pk>/editar/', views.editar_pedido, name='editar_pedido'),

    path('<int:pk>/', views.detalhe_pedido, name='detalhe_pedido'),

]