# Generated by Django 5.0.6 on 2024-07-01 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_user_userprofile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='type',
            new_name='user_type',
        ),
    ]
