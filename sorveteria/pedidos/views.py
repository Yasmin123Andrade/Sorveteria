from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedidos
from .forms import PedidosForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def listar_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {
        'pedidos': pedidos
    })


@login_required
def criar_pedido(request):
    if request.method == 'POST':
        form = PedidosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')

    else:
        form = PedidosForm()

    return render(request, 'pedidos/criar_pedido.html', {
        'form': form
    })


def detalhe_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)

    return render(request, 'pedidos/detalhe_pedido.html', {
        'pedido': pedido
    })


@login_required
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)

    if request.method == 'POST':
        form = PedidosForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('detalhe_pedido', pk=pedido.pk)
    else:
        form = PedidosForm(instance=pedido)

    return render(request, 'pedidos/editar_pedido.html', {
        'form': form,
        'pedido': pedido
    })