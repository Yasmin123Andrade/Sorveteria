from django.contrib import admin
from django import forms
from .models import Produto


class ProdutoAdminForm(forms.ModelForm):
    criado_por_nome = forms.CharField(
        label='Criado por',
        disabled=True,
        required=False,
    )

    class Meta:
        model = Produto
        fields = ('descricao', 'valor', 'criado_por_nome')

class ProdutoAdmin(admin.ModelAdmin):
    form = ProdutoAdminForm
    list_display = ('id', 'descricao', 'valor', 'nome_criador')
    search_fields = ('descricao',)

    def get_form(self, request, obj=None, **kwargs):
        form_class = super().get_form(request, obj, **kwargs)

        class RequestProdutoAdminForm(form_class):
            def __init__(self, *args, **form_kwargs):
                super().__init__(*args, **form_kwargs)
                criador = self.instance.criado_por or request.user
                pessoa = getattr(criador, 'pessoa', None)
                nome = pessoa.nome if pessoa else criador.username
                self.fields['criado_por_nome'].initial = nome

        return RequestProdutoAdminForm

    @admin.display(description='Criado por')
    def nome_criador(self, obj):
        if not obj.criado_por:
            return '-'

        pessoa = getattr(obj.criado_por, 'pessoa', None)
        return pessoa.nome if pessoa else obj.criado_por.username

    def save_model(self, request, obj, form, change):
        user = request.user
        obj.criado_por = user
        super().save_model(request, obj, form, change)

admin.site.register(Produto, ProdutoAdmin)
