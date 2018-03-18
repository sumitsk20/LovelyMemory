# Generated by Django 2.0.3 on 2018-03-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=100)),
                ('customer_location', models.URLField(default='', max_length=500)),
                ('customer_note', models.TextField(default='', max_length=1500)),
                ('customer_deliver_date', models.DateField(blank=True, default=1970.0, null=True)),
                ('customer_deliver_time', models.TimeField(blank=True, default='', null=True)),
                ('customer_phone_number', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1500)),
                ('image', models.ImageField(blank=True, upload_to='product_image')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('modificationTime', models.DateField(auto_now=True)),
                ('type_product', models.CharField(choices=[('BL', 'balloon'), ('GF', 'gift'), ('FW', 'flower')], default='FW', max_length=2)),
            ],
        ),
    ]
