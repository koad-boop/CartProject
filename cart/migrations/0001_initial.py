# Generated by Django 5.0.6 on 2024-06-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pass1', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('image', models.FileField(null=True, upload_to='uploads/users/')),
            ],
        ),
    ]
