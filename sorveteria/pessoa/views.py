from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'pessoa/lista_pessoas.html', {
        'pessoas': pessoas
    })


def criar_pessoa(request):

    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()

            # Depois de cadastrar, volta para o login
            return redirect('login')

    else:
        form = PessoaForm()

    return render(request, 'pessoa/criar_pessoa.html', {
        'form': form
    })


def detalhe_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)

    return render(request, 'pessoa/detalhe_pessoa.html', {
        'pessoa': pessoa
    })