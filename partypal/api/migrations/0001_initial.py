# Generated by Django 4.2 on 2023-05-08 16:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(default=datetime.datetime(2023, 6, 10, 10, 30))),
                ('end_date', models.DateTimeField(default=datetime.datetime(2023, 6, 10, 12, 0))),
                ('location', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='event_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guests', models.ManyToManyField(blank=True, default=[], related_name='registered_guests', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_hosted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('contact_name', models.CharField(default='', max_length=100)),
                ('contact_email', models.EmailField(default='', max_length=100)),
                ('contact_phone', models.CharField(default='', max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('event', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='api.event')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('events_hosted', models.ManyToManyField(blank=True, default=[], related_name='hosts', to='api.event')),
                ('events_hosting', models.ManyToManyField(blank=True, default=[], related_name='hosted_events', to='api.event')),
                ('user', models.OneToOneField(default='Amaino', on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.venue'),
        ),
    ]
