# Generated by Django 4.2.7 on 2024-11-28 09:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserApp', '0003_notification_frommessage_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='save',
            unique_together={('user', 'post')},
        ),
    ]
