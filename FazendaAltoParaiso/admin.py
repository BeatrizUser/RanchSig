from django.contrib import admin
from .models import Animal, Saude, Reproducao, Peso, Alimentacao, Movimentacao, Economia, Abate, Observacao

class SaudeInline(admin.StackedInline):
    model = Saude

class ReproducaoInline(admin.StackedInline):
    model = Reproducao
    fk_name = 'animal'

class PesoInline(admin.StackedInline):
    model = Peso

class AlimentacaoInline(admin.StackedInline):
    model = Alimentacao

class MovimentacaoInline(admin.StackedInline):
    model = Movimentacao

class EconomiaInline(admin.StackedInline):
    model = Economia

class AbateInline(admin.StackedInline):
    model = Abate

class ObservacaoInline(admin.StackedInline):
    model = Observacao

class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações Gerais', {'fields': ['numero_identificacao', 'data_nascimento', 'raca', 'pedigree', 'historico_genetico']}),
        ('Pais', {'fields': ['pai', 'mae']}),
    ]
    inlines = [
        SaudeInline,
        ReproducaoInline,
        PesoInline,
        AlimentacaoInline,
        MovimentacaoInline,
        EconomiaInline,
        AbateInline,
        ObservacaoInline,
    ]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = []
        return super().change_view(request, object_id, form_url, extra_context)

admin.site.register(Animal, AnimalAdmin)
