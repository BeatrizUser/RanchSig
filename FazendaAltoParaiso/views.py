from django.shortcuts import render
from .models import Animal, Saude, Reproducao, Peso, Alimentacao, Movimentacao, Economia, Abate, Observacao

def dashboard(request):
    animals = Animal.objects.all()
    # Consultar outros modelos necessários
    
    context = {
        'animals': animals,
        # Adicionar outros dados ao contexto
    }
    
    return render(request, 'dashboard.html', context)
