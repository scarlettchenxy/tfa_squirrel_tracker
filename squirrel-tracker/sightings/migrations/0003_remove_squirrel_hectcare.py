# Generated by Django 3.0 on 2019-12-09 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_squirrel_hectcare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='Hectcare',
        ),
    ]