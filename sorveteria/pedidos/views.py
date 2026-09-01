from django.shortcuts import render, redirect
from .models import Pedidos
from .forms import PedidosForm
def listar_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

def criar_pedido(request):
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidosForm()
    return render(request, 'pedidos/criar_pedido.html', {'form': form})