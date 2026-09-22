from django.urls import path, include

from . import views

from django.conf import settings


urlpatterns = [

    path(
        '',
        views.lista_pessoas,
        name='lista_pessoas'
    ),

    path(
        'novo/',
        views.criar_pessoa,
        name='criar_pessoa'
    ),

    path(
        '<int:pk>/',
        views.detalhe_pessoa,
        name='detalhe_pessoa'
    ),

    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),

]