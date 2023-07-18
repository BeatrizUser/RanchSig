from django.contrib import admin
from django.contrib.admin import helpers
from django.utils.translation import gettext as _
from .models import Animal, Saude, Reproducao, Peso, Alimentacao, Movimentacao, Economia, Abate, Observacao

class CustomAdminSite(admin.AdminSite):
    site_title = 'Gestão Fazenda Alto Paraíso'
    site_header = 'Administração Fazenda Alto Paraíso'
    index_title = 'Administração Fazenda Alto Paraíso'

admin.site = CustomAdminSite()

class SaudeInline(admin.StackedInline):
    model = Saude
    extra = 0

class ReproducaoInline(admin.StackedInline):
    model = Reproducao
    fk_name = 'animal'
    extra = 0

class PesoInline(admin.StackedInline):
    model = Peso
    extra = 0

class AlimentacaoInline(admin.StackedInline):
    model = Alimentacao
    extra = 0

class MovimentacaoInline(admin.StackedInline):
    model = Movimentacao
    extra = 0

class EconomiaInline(admin.StackedInline):
    model = Economia
    extra = 0

class AbateInline(admin.StackedInline):
    model = Abate
    extra = 0

class ObservacaoInline(admin.StackedInline):
    model = Observacao
    extra = 0

class AnimalAddView(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = []
        return super().add_view(request, form_url, extra_context)

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

    def get_add_view(self, request):
        return AnimalAddView.as_view(
            # Passar as mesmas variáveis de contexto do ModelAdmin original
            extra_context=self.get_extra_context(request)
        )(request)

admin.site.register(Animal, AnimalAdmin)
