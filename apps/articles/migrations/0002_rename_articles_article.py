# Generated by Django 4.2.2 on 2023-06-09 07:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Articles",
            new_name="Article",
        ),
    ]
