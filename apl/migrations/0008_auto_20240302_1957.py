# Generated by Django 3.2.12 on 2024-03-02 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0007_cat_news_news_sub_cat_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.RemoveField(
            model_name='news',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='sub_cat_news',
            name='category',
        ),
        migrations.DeleteModel(
            name='Cat_News',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Sub_Cat_News',
        ),
    ]
