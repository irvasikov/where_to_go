# Generated by Django 3.2.5 on 2021-07-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_afisha', '0004_places_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='place_id',
            field=models.CharField(max_length=100),
        ),
    ]