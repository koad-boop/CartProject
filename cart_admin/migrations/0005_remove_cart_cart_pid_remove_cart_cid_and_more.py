# Generated by Django 5.0.6 on 2024-06-08 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('cart_admin', '0004_cart_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_pid',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='cust_id',
            field=models.ForeignKey(null='TRUE', on_delete=django.db.models.deletion.CASCADE, to='cart.customer'),
            preserve_default='TRUE',
        ),
        migrations.AddField(
            model_name='cart',
            name='pro_id',
            field=models.ForeignKey(null='TRUE', on_delete=django.db.models.deletion.CASCADE, to='cart_admin.product'),
            preserve_default='TRUE',
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
