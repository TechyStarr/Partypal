# Generated by Django 4.2 on 2023-05-08 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_event_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]
