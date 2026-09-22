from django.urls import path, include

from . import views

from django.conf import settings

urlpatterns = [

    path('', views.listar_pedidos, name='lista_pedidos'),

    path('novo/', views.criar_pedido, name='criar_pedido'),

    path('<int:pk>/', views.detalhe_pedido, name='detalhe_pedido'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('home/', views.home, name='home'),

]