# Generated by Django 2.0.5 on 2018-08-20 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dolar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dolar',
            name='id',
        ),
        migrations.AlterField(
            model_name='dolar',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]