# Generated by Django 2.2.6 on 2019-10-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='fecha',
            field=models.DateField(primary_key=True, serialize=False, unique=True),
        ),
    ]