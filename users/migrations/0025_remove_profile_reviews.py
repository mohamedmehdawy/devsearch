# Generated by Django 4.0.4 on 2023-01-29 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_profile_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reviews',
        ),
    ]
