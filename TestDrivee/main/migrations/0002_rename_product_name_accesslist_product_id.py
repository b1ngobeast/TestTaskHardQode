# Generated by Django 5.0.2 on 2024-02-29 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesslist',
            old_name='product_name',
            new_name='product_id',
        ),
    ]
