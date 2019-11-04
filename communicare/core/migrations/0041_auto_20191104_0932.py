# Generated by Django 2.1.8 on 2019-11-04 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20191104_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lead')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='descrição')),
                ('date', models.DateTimeField(verbose_name='data/hora')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.City', verbose_name='cidade')),
                ('participants', models.ManyToManyField(blank=True, through='core.Audience', to='core.Lead', verbose_name='participantes')),
            ],
            options={
                'verbose_name': 'palestra',
            },
        ),
        migrations.AddField(
            model_name='audience',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lecture'),
        ),
    ]
