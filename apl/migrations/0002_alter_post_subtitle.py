# Generated by Django 3.2.12 on 2024-02-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
