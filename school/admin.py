from django.contrib import admin
from .models import (Student, Class, TypeOfClass, Teacher,
                     Discipline, Task, Curriculum, Mark)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("family_name", "first_name", "second_name", "birthday",
                    "address")


class ClassAdmin(admin.ModelAdmin):
    list_display = ("group", "class_number")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("family_name", "first_name", "second_name", "birthday",
                    "address", "salary", "gender")


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "hours")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "start_date", "end_date", "commentary")


admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(TypeOfClass)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Curriculum)
# Register your models here.
