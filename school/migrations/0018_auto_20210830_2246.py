# Generated by Django 3.1.7 on 2021-08-30 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20210827_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('family_name',)},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('family_name',)},
        ),
    ]
