# Generated by Django 5.0.4 on 2024-05-12 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_remove_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
