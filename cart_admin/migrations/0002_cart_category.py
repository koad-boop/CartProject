# Generated by Django 5.0.6 on 2024-06-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_pid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('image', models.FileField(upload_to='uploads/cart/')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=100)),
            ],
        ),
    ]
