# Generated by Django 4.0.2 on 2022-04-13 09:10

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_pegawai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='foto',
            field=models.ImageField(blank=True, upload_to=home.models.rename),
        ),
    ]