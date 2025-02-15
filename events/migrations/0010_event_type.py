# Generated by Django 4.2.17 on 2025-01-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_organizer_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('subject', 'By Subject'), ('type', 'By Event Type'), ('audience', 'By Audience'), ('purpose', 'By Purpose'), ('tags', 'By Tags'), ('experience', 'By Experience Type')], default='subject', max_length=20),
        ),
    ]
