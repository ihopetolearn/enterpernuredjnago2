# Generated by Django 5.0.4 on 2024-05-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_remove_article_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create',
            field=models.DateField(auto_now=True),
        ),
    ]
