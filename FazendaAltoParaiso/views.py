from django.shortcuts import render
from django.db import models
from .models import Animal, Saude, Reproducao, Peso, Alimentacao, Movimentacao, Economia, Abate, Observacao

def dashboard(request):
    animals = Animal.objects.all()
    # Consultar outros modelos necessários
    
    racas = Animal.objects.values('raca').annotate(quantidade=models.Count('id'))

    context = {
        'animals': animals,
        'racas': racas,
        # Adicionar outros dados ao contexto
    }
    
    return render(request, 'dashboard.html', context)

