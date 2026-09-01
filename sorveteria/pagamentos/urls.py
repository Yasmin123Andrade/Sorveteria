from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pagamentos, name='lista_pagamentos'),
    path('novo/', views.criar_pagamento, name='criar_pagamento'),
]