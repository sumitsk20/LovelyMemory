# Generated by Django 2.0.2 on 2018-02-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0003_auto_20180222_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('BL', 'balloon'), ('GF', 'gift'), ('FW', 'flower')], default='FW', max_length=2),
        ),
    ]