# Generated by Django 2.1.8 on 2019-08-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_event_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('tre_ora', 'Treinamento de Oratória'), ('cur_hip', 'Curso de Hipnose Clínica'), ('tre_iem', 'Treinamento de Inteligência Emocional')], max_length=7, verbose_name='tipo'),
        ),
    ]
