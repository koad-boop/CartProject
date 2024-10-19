# Generated by Django 5.0.6 on 2024-06-01 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_admin', '0002_cart_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('des', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='uploads/products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart_admin.category')),
            ],
        ),
    ]
