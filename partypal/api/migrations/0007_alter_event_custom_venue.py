# Generated by Django 4.2 on 2023-05-09 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='custom_venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_events', to='api.venue'),
        ),
    ]
