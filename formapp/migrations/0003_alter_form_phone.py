# Generated by Django 4.1.8 on 2023-09-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_alter_form_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
