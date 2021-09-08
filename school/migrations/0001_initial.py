# Generated by Django 3.1.7 on 2021-09-08 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30)),
                ('class_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40)),
                ('hours', models.IntegerField()),
                ('slug', models.SlugField(default='some-slug')),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.class')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('family_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=60)),
                ('birthday', models.DateField()),
                ('salary', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('family_name',),
            },
        ),
        migrations.CreateModel(
            name='TypeOfClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_class', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Type of class',
                'verbose_name_plural': 'Types of classes',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('commentary', models.TextField()),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.class')),
                ('discipline_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.discipline')),
                ('teacher_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
            options={
                'ordering': ('end_date',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('family_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=60)),
                ('birthday', models.DateField()),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.class')),
            ],
            options={
                'ordering': ('family_name',),
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_score', models.IntegerField()),
                ('student_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('task_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.task')),
            ],
        ),
        migrations.AddField(
            model_name='discipline',
            name='teacher_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.class')),
                ('discipline_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.discipline')),
                ('teacher_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='type_of_class',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.typeofclass'),
        ),
    ]
