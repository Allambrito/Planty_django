# Generated by Django 4.0.5 on 2022-06-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tiendita', '0011_alter_producto_foto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Foto_producto',
            field=models.ImageField(blank=True, null=True, upload_to='vitrina'),
        ),
    ]
