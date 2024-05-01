# Generated by Django 5.0.4 on 2024-04-29 17:22

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task_date_task_description_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=myapp.models.get_current_date),
        ),
    ]
