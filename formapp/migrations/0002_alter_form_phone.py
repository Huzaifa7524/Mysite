# Generated by Django 4.1.8 on 2023-09-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.IntegerField(),
        ),
    ]