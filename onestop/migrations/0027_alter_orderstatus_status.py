# Generated by Django 4.0.4 on 2022-12-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestop', '0026_alter_orderstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Dispatched', 'Dispatched'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], default='Packed', max_length=50),
        ),
    ]
