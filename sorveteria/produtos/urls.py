from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.criar_produto, name='criar_produto'),
    path('accounts/', include('django.contrib.auth.urls')),
]