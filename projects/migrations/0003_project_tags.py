# Generated by Django 3.1.4 on 2022-04-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220425_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.Tag'),
        ),
    ]
