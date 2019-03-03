from django.shortcuts import render


def usuario(request):
    return render(request, 'usuarios.html')
