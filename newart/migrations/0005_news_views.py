# Generated by Django 3.2.12 on 2024-03-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newart', '0004_auto_20240303_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
