# Generated by Django 2.2.6 on 2019-10-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standup', '0005_standup_rebuild_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='discord_channel_id',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='discord_guild_id',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='standup',
            name='pinned_message_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
