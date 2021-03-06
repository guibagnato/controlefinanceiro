# Generated by Django 2.2.3 on 2019-07-18 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('carteira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Peso')),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Acao')),
                ('definicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteira.Definicao')),
            ],
            options={
                'verbose_name': 'Composições',
                'ordering': ('definicao__name', 'acao__code', 'weight'),
                'verbose_name_plural': 'Composição',
            },
        ),
    ]
