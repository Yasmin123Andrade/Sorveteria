from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas dos seus aplicativos:
    path('pessoas/', include('pessoa.urls')),
    path('produtos/', include('produtos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('pagamentos/', include('pagamentos.urls')),
]