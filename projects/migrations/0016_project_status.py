# Generated by Django 4.0.4 on 2023-01-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
