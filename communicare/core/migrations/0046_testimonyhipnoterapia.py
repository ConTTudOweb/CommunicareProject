# Generated by Django 2.1.8 on 2020-04-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20200413_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonyHipnoterapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_video_youtube', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'depoimento hipnoterapia',
                'verbose_name_plural': 'depoimentos hipnoterapia',
            },
        ),
    ]
