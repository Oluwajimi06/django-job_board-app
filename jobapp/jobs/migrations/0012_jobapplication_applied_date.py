# Generated by Django 5.0.4 on 2024-04-14 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='applied_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 14, 10, 5, 4, 870916, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
