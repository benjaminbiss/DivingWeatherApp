# Generated by Django 3.2.8 on 2021-12-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_pk', models.IntegerField(blank=True, null=True)),
                ('diver_pk', models.IntegerField(blank=True, null=True)),
                ('reply', models.CharField(max_length=250)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('dislikes', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
