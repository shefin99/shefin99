# Generated by Django 4.1.3 on 2022-12-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_product_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offers',
        ),
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
