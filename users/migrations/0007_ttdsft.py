# Generated by Django 4.0.4 on 2022-07-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_ttt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ttdsft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
