# Generated by Django 5.0.3 on 2024-03-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0002_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birsday',
            field=models.DateField(blank=True, null=True),
        ),
    ]