# Generated by Django 4.2.5 on 2023-09-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=True, verbose_name='Is customer'),
        ),
    ]
