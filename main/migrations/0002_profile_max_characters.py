# Generated by Django 3.0.6 on 2020-05-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='max_characters',
            field=models.IntegerField(default=3),
        ),
    ]