# Generated by Django 4.0.4 on 2022-07-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20220525_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='projects.tag'),
        ),
    ]
