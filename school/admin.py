from django.contrib import admin
from .models import Student, Class, TypeOfClass, Teacher, Discipline


class StudentAdmin(admin.ModelAdmin):
    list_display = ("family_name", "first_name", "second_name", "birthday", "address")


class ClassAdmin(admin.ModelAdmin):
    list_display = ("group", "class_number")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("family_name", "first_name", "second_name", "birthday",
                    "address", "salary", "gender")


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "hours")


admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(TypeOfClass)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Discipline, DisciplineAdmin)
# Register your models here.
