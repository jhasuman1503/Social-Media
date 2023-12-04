# Generated by Django 4.0 on 2022-09-09 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_users_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='dateofpost',
            new_name='dateoffollow',
        ),
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 9, 13, 54, 8, 491750), null=True),
        ),
    ]