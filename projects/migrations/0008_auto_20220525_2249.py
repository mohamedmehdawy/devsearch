# Generated by Django 3.1.4 on 2022-05-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]