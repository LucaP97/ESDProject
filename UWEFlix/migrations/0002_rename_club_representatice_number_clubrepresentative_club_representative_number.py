# Generated by Django 4.1.5 on 2023-01-13 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubrepresentative',
            old_name='club_representatice_number',
            new_name='club_representative_number',
        ),
    ]