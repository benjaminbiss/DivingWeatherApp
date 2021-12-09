# Generated by Django 3.2.8 on 2021-12-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20211208_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name='locations',
            name='longitude',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
