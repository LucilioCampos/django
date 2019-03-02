from django.shortcuts import render
from .models import Produto


def home(request):
    nome = 'Django moc'
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'nome': nome, 'produtos': produtos})


def produto(request, codigo):
    cod_prod = Produto.objects.get(id=codigo)
    return render(request, 'produtos.html', {'produto': cod_prod})
