# Generated by Django 4.0.4 on 2022-12-14 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestop', '0024_currseller_s_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('prod_id', models.IntegerField()),
                ('listedBy', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=200)),
                ('status', models.CharField(choices=[('Not Dispatched', 'Not Dispatched'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered')], default='Not Dispatched', max_length=50)),
            ],
        ),
    ]
