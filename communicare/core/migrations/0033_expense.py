# Generated by Django 2.1.8 on 2019-09-23 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_registration_net_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='descrição')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='valor')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Event', verbose_name='evento')),
            ],
            options={
                'verbose_name': 'despesa',
            },
        ),
    ]
