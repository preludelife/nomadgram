# Generated by Django 2.0.5 on 2018-07-03 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_notification_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]