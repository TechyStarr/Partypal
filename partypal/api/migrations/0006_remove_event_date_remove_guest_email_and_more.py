# Generated by Django 4.2 on 2023-05-07 08:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_event_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='email',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='event',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='name',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='host',
            name='email',
        ),
        migrations.RemoveField(
            model_name='host',
            name='event',
        ),
        migrations.RemoveField(
            model_name='host',
            name='name',
        ),
        migrations.RemoveField(
            model_name='host',
            name='phone',
        ),
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 10, 12, 0)),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='event_images/'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 10, 10, 30)),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.venue'),
        ),
        migrations.AddField(
            model_name='guest',
            name='bio',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='guest',
            name='user',
            field=models.OneToOneField(default='Amaino', on_delete=django.db.models.deletion.CASCADE, related_name='guests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='host',
            name='bio',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='host',
            name='events_hosted',
            field=models.ManyToManyField(blank=True, default=[], related_name='hosts', to='api.event'),
        ),
        migrations.AddField(
            model_name='host',
            name='events_hosting',
            field=models.ManyToManyField(blank=True, default=[], related_name='hosted_events', to='api.event'),
        ),
        migrations.AddField(
            model_name='host',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='host',
            name='user',
            field=models.OneToOneField(default='Amaino', on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='venue',
            name='contact_email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='venue',
            name='contact_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='venue',
            name='contact_phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='venue',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(blank=True, default=[], related_name='registered_guests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venue',
            name='event',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='api.event'),
        ),
    ]