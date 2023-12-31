# Generated by Django 4.1 on 2023-07-13 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacao', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('raca', models.CharField(max_length=255)),
                ('pedigree', models.CharField(max_length=255)),
                ('historico_genetico', models.TextField()),
                ('mae', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filhos_maternos', to='FazendaAltoParaiso.animal')),
                ('pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filhos_paternos', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Saude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historico_vacinacao', models.TextField(blank=True)),
                ('tratamentos', models.TextField(blank=True)),
                ('exames', models.TextField(blank=True)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='saude', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Reproducao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cobertura', models.DateField(blank=True, null=True)),
                ('data_inseminacao', models.DateField(blank=True, null=True)),
                ('data_parto', models.DateField(blank=True, null=True)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reproducao', to='FazendaAltoParaiso.animal')),
                ('mae', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filhos_maternos_reproducao', to='FazendaAltoParaiso.animal')),
                ('pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filhos_paternos_reproducao', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pesagem', models.DateField()),
                ('peso', models.FloatField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_observacao', models.DateField()),
                ('texto_observacao', models.TextField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observacoes', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_movimentacao', models.DateField()),
                ('local_origem', models.CharField(max_length=255)),
                ('local_destino', models.CharField(max_length=255)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimentacoes', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Economia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custo_aquisicao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('custo_alimentacao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('custo_tratamentos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receita_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='economia', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Alimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alimentacao', models.DateField()),
                ('tipo_alimento', models.CharField(max_length=255)),
                ('quantidade', models.FloatField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimentacao', to='FazendaAltoParaiso.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Abate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_abate', models.DateField()),
                ('peso_carcaca', models.FloatField()),
                ('valor_carcaca', models.DecimalField(decimal_places=2, max_digits=10)),
                ('classificacao_carne', models.CharField(max_length=255)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abate', to='FazendaAltoParaiso.animal')),
            ],
        ),
    ]
