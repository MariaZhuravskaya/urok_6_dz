# Generated by Django 4.2.4 on 2023-09-06 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='publication',
            new_name='is_publication',
        ),
    ]
