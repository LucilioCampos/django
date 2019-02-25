from django.shortcuts import render
from .models import Produto

# Create your views here.


def home(request):
    nome = 'Django MOC'
    produtos = Produto.objects.all()

    return render(request, 'produtos.html', {'produtos': produtos})
