# Generated by Django 3.1.1 on 2020-09-18 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='image',
        ),
        migrations.AddField(
            model_name='unit',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='units_images/', verbose_name='Unit Main Image'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='units_images/')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.unit')),
            ],
        ),
    ]
