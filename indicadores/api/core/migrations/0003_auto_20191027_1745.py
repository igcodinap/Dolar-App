# Generated by Django 2.2.6 on 2019-10-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191027_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolar',
            name='fecha',
            field=models.DateTimeField(primary_key=True, serialize=False, unique=True),
        ),
    ]
