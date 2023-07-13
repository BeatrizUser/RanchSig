from django.db import models

RAÇA_CHOICES = [
    ('nelore', 'Nelore'),
    ('angus', 'Angus'),
    ('brahman', 'Brahman'),
    ('senepol', 'Senepol'),
    ('guzerá', 'Guzerá'),
    ('simental', 'Simental'),
    ('limousin', 'Limousin'),
    ('tabapuã', 'Tabapuã'),
    ('hereford', 'Hereford'),
    ('charolês', 'Charolês'),
]

PEDIGREE_CHOICES = [
    ('registrado', 'Registrado'),
    ('puro-sangue', 'Puro-sangue'),
    ('mestiço', 'Mestiço'),
    ('sem-pedigree', 'Sem Pedigree'),
    ('po', 'PO (Puro de Origem)'),
]

TIPO_ALIMENTO_CHOICES = [
    ('ração', 'Ração'),
    ('pasto', 'Pasto'),
    ('silagem', 'Silagem'),
    ('feno', 'Feno'),
    ('grãos', 'Grãos'),
    ('suplemento-mineral', 'Suplemento mineral'),
    ('mistura-total', 'Mistura total'),
    ('concentrado', 'Concentrado'),
]

LOCAIS_FAZENDA_CHOICES = [
    ('piquete-1', 'Piquete 1'),
    ('piquete-2', 'Piquete 2'),
    ('piquete-3', 'Piquete 3'),
    ('pasto-a', 'Pasto A'),
    ('pasto-b', 'Pasto B'),
    ('área-de-manejo', 'Área de Manejo'),
    ('curral-principal', 'Curral Principal'),
    ('curral-de-engorda', 'Curral de Engorda'),
    ('sombradouro', 'Sombreadouro'),
    ('cocho-de-alimentação', 'Cocho de Alimentação'),
]

class Animal(models.Model):
    numero_identificacao = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    raca = models.CharField(max_length=255, choices=RAÇA_CHOICES)
    pedigree = models.CharField(max_length=255, choices=PEDIGREE_CHOICES)
    historico_genetico = models.TextField()
    pai = models.ForeignKey('self', on_delete=models.CASCADE, related_name='filhos_paternos', null=True, blank=True)
    mae = models.ForeignKey('self', on_delete=models.CASCADE, related_name='filhos_maternos', null=True, blank=True)

class Saude(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='saude')
    historico_vacinacao = models.TextField(blank=True)
    tratamentos = models.TextField(blank=True)
    exames = models.TextField(blank=True)

class Reproducao(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='reproducao')
    mae = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='filhos_maternos_reproducao', null=True, blank=True)
    pai = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='filhos_paternos_reproducao', null=True, blank=True)
    data_cobertura = models.DateField(null=True, blank=True)
    data_inseminacao = models.DateField(null=True, blank=True)
    data_parto = models.DateField(null=True, blank=True)

class Peso(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='pesos')
    data_pesagem = models.DateField()
    peso = models.FloatField()

class Alimentacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='alimentacao')
    data_alimentacao = models.DateField()
    tipo_alimento = models.CharField(max_length=255, choices=TIPO_ALIMENTO_CHOICES)
    quantidade = models.FloatField()

class Movimentacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='movimentacoes')
    data_movimentacao = models.DateField()
    local_origem = models.CharField(max_length=255, choices=LOCAIS_FAZENDA_CHOICES)
    local_destino = models.CharField(max_length=255, choices=LOCAIS_FAZENDA_CHOICES)

class Economia(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='economia')
    custo_aquisicao = models.DecimalField(max_digits=10, decimal_places=2)
    custo_alimentacao = models.DecimalField(max_digits=10, decimal_places=2)
    custo_tratamentos = models.DecimalField(max_digits=10, decimal_places=2)
    receita_venda = models.DecimalField(max_digits=10, decimal_places=2)

class Abate(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='abate')
    data_abate = models.DateField()
    peso_carcaca = models.FloatField()
    valor_carcaca = models.DecimalField(max_digits=10, decimal_places=2)
    classificacao_carne = models.CharField(max_length=255)

class Observacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='observacoes')
    data_observacao = models.DateField()
    texto_observacao = models.TextField()
