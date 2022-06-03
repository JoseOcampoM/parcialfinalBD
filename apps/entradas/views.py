from django.shortcuts import render, redirect
from apps.entradas.formentrada import FormEntrada
from apps.entradas.models import Entrada
# Create your views here.

def inicio(request):
    entrada = Entrada.objects.all().order_by('id')
    return render(request,'paginas/entrada.html', {'entrada': entrada})

def create(request):
    if request.method == 'POST':
        form = FormEntrada(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = FormEntrada()
        return render(request,'paginas/entradaform.html', {'form': form})