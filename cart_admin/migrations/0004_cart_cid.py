# Generated by Django 5.0.6 on 2024-06-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_admin', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cid',
            field=models.CharField(max_length=20, null='True'),
            preserve_default='True',
        ),
    ]
