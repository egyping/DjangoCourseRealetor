# Generated by Django 3.1.1 on 2020-09-18 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0005_unit_num_bedrooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='main_image',
            new_name='image',
        ),
    ]
