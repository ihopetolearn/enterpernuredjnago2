# Generated by Django 5.0.4 on 2024-05-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='added by paiman'),
            preserve_default=False,
        ),
    ]
