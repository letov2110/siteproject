# Generated by Django 3.2.12 on 2024-03-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newart', '0003_auto_20240303_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(to='newart.Cat_News'),
        ),
    ]
