# Generated by Django 2.1.8 on 2020-04-13 13:56

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_event_external_subscriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(help_text='Imagem quadrada com no mínimo 170px', max_length=255, verbose_name='imagem')),
            ],
            options={
                'verbose_name': 'imagem da galeria',
                'verbose_name_plural': 'imagens da galeria',
            },
        ),
    ]
