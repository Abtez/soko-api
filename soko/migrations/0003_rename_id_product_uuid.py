# Generated by Django 3.2.9 on 2021-11-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soko', '0002_auto_20211121_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='uuid',
        ),
    ]
