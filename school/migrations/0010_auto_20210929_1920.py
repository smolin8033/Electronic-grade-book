# Generated by Django 3.1.7 on 2021-09-29 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20210929_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='class_id',
            new_name='grade',
        ),
    ]
