# Generated by Django 2.0.2 on 2018-02-22 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_auto_20180222_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='changeTime',
            new_name='modificationTime',
        ),
    ]