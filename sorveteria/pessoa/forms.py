from django import forms
from django.contrib.auth.models import User
from .models import Pessoa


class PessoaForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        required=True,
        label="Usuário"
    )

    password = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput
    )

    password_confirm = forms.CharField(
        required=True,
        label="Confirmar senha",
        widget=forms.PasswordInput
    )


    class Meta:

        model = Pessoa

        fields = [
            'username',
            'password',
            'password_confirm',
            'cpf',
            'nome',
            'telefone',
            'rua',
            'bairro',
            'numero',
            'cep',
            'cidade',
            'estado'
        ]

        labels = {
            'cpf': 'CPF',
            'nome': 'Nome completo',
            'telefone': 'Telefone',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'numero': 'Número',
            'cep': 'CEP',
            'cidade': 'Cidade',
            'estado': 'Estado',
        }


    def clean_username(self):

        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():

            raise forms.ValidationError(
                "Este nome de usuário já está em uso. Escolha outro."
            )

        return username


    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if (
            password
            and password_confirm
            and password != password_confirm
        ):

            self.add_error(
                'password_confirm',
                'As senhas não coincidem.'
            )

        return cleaned_data


    def save(self, commit=True):

        pessoa = super().save(commit=False)

        pessoa.username = self.cleaned_data['username']

        pessoa.set_password(
            self.cleaned_data['password']
        )

        if commit:
            pessoa.save()

        return pessoa


class PessoaEditForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        label="Nova senha",
        widget=forms.PasswordInput
    )

    password_confirm = forms.CharField(
        required=False,
        label="Confirmar nova senha",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Pessoa
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'cpf',
            'nome',
            'telefone',
            'rua',
            'bairro',
            'numero',
            'cep',
            'cidade',
            'estado'
        ]

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Este nome de usuário já está em uso. Escolha outro."
            )
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            self.add_error(
                'password_confirm',
                'As senhas não coincidem.'
            )
        return cleaned_data

    def save(self, commit=True):
        pessoa = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            pessoa.set_password(password)
        if commit:
            pessoa.save()
        return pessoa