from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sobre/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contato/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    
    # Rotas dos seus aplicativos:
    path('pessoas/', include('pessoa.urls')),
    path('produtos/', include('produtos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('pagamentos/', include('pagamentos.urls')),
]