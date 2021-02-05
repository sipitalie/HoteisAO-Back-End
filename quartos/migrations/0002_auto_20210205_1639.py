# Generated by Django 3.0.5 on 2021-02-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quartos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarto',
            name='Numero_do_quarto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quarto',
            name='Status',
            field=models.CharField(choices=[('Ocupado', 'Ocupado'), ('Disponivel', 'Disponivel'), ('Outros', 'Outros')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]