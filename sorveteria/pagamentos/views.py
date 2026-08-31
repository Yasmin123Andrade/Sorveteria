from django.shortcuts import render, redirect
from .models import Pagamento
from .forms import PagamentoForm

def lista_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamentos/lista_pagamentos.html', {'pagamentos': pagamentos})

def criar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pagamentos')
    else:
        form = PagamentoForm()
    return render(request, 'pagamentos/criar_pagamento.html', {'form': form})