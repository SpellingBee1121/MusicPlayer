# Generated by Django 4.1 on 2023-05-10 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Songs",
            new_name="Song",
        ),
    ]
