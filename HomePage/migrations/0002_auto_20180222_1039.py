# Generated by Django 2.0.2 on 2018-02-22 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date',
            new_name='changeTime',
        ),
    ]