# Generated by Django 4.2 on 2023-05-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_venue_event_event_custom_venue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='event_images/'),
        ),
    ]