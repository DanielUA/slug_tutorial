# Generated by Django 4.2.2 on 2023-06-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_rename_articles_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="slug",
            field=models.SlugField(null=True),
        ),
    ]
