from django.urls import path, include
from .views import usuario

urlpatterns = [
    path('usuario/', usuario),
]
