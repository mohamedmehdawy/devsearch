# Generated by Django 3.1.4 on 2022-05-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20220525_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
