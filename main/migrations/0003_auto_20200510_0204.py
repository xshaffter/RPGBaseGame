# Generated by Django 3.0.6 on 2020-05-10 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_max_characters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='equipment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.CharacterEquipment'),
        ),
    ]
