# Generated by Django 4.1.5 on 2023-01-13 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlix', '0003_rename_agerating_film_age_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]