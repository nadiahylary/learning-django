# Generated by Django 4.1.7 on 2023-03-07 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0007_alter_address_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
