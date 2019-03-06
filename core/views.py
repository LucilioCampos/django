from django.shortcuts import render

from core.models import Usuario


def usuarios(request):
    usuarios = Usuario
    return render('usuarios.html', {'usuarios': usuarios})
