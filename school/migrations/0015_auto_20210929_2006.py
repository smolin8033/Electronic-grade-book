# Generated by Django 3.1.7 on 2021-09-29 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_auto_20210929_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='task_id',
            new_name='task',
        ),
    ]
