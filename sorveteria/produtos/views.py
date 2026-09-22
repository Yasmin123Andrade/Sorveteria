from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

from .forms import ProdutoForm

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})


@login_required
def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})


@login_required
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_produtos')

    else:
        form = ProdutoForm()

    return render(request, 'produtos/criar_produto.html', {'form': form})

