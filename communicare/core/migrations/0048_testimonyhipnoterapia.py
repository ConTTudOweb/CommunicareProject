# Generated by Django 2.1.8 on 2020-04-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_delete_testimonyhipnoterapia'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonyHipnoterapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('id_video_youtube', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'depoimento hipnoterapia',
                'verbose_name_plural': 'depoimentos hipnoterapia',
            },
        ),
    ]
