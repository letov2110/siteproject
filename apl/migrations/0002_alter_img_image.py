# Generated by Django 5.0.3 on 2024-04-17 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='image',
            field=models.ImageField(upload_to='upload/apl'),
        ),
    ]