# Generated by Django 2.1.7 on 2019-02-15 14:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20190212_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='imagem'),
        ),
    ]
