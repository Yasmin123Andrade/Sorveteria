from django.contrib import messages
from django.shortcuts import redirect, render


def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        mensagem = request.POST.get('message', '').strip()

        if not nome or not email or not mensagem:
            messages.error(request, 'Preencha nome, e-mail e mensagem.')
        else:
            messages.success(request, 'Mensagem enviada. Em breve entraremos em contato.')
            return redirect('contact')

    return render(request, 'contact.html')
