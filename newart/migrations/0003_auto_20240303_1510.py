# Generated by Django 3.2.12 on 2024-03-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newart', '0002_alter_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='Sub_Cat_News',
        ),
    ]
