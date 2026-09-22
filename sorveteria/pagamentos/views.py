from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagamento
from .forms import PagamentoForm
from django.contrib.auth.decorators import login_required


@login_required
def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamentos/lista_pagamentos.html', {
        'pagamentos': pagamentos
    })


@login_required
def criar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_pagamentos')
        else:
            print(form.errors)

    else:
        form = PagamentoForm()

    return render(request, 'pagamentos/criar_pagamento.html', {
        'form': form
    })


def detalhe_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)

    return render(request, 'pagamentos/detalhe_pagamento.html', {
        'pagamento': pagamento
    })


@login_required
def editar_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)

        if form.is_valid():
            form.save()
            return redirect('detalhe_pagamento', pk=pagamento.pk)

    else:
        form = PagamentoForm(instance=pagamento)

    return render(request, 'pagamentos/editar_pagamento.html', {
        'form': form,
        'pagamento': pagamento
    })