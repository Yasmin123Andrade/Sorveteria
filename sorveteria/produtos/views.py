from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

from .forms import ProdutoForm

from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    return render(request, 'home.html')


@login_required
@permission_required('produtos.view_produto', raise_exception=True)
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})


@login_required
@permission_required('produtos.view_produto', raise_exception=True)
def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})


@login_required
@permission_required('produtos.change_produto', raise_exception=True)
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('detalhe_produto', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/editar_produto.html', {
        'form': form,
        'produto': produto
    })


@login_required
@permission_required('produtos.add_produto', raise_exception=True)
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_produtos')

    else:
        form = ProdutoForm()

    return render(request, 'produtos/criar_produto.html', {'form': form})

