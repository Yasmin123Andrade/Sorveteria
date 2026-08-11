from django.contrib import admin
from .models import Pessoa  # e os outros modelos do app pessoa

admin.site.register(Pessoa)