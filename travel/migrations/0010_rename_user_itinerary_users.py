# Generated by Django 5.0 on 2024-03-14 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_itinerary_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='user',
            new_name='users',
        ),
    ]
