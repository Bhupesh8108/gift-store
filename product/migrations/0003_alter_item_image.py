# Generated by Django 4.1.7 on 2023-04-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_items_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
