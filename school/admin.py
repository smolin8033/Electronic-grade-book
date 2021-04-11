from django.contrib import admin
from .models import Student, Class, TypeOfClass


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "family_name", "birthday", "address")


class ClassAdmin(admin.ModelAdmin):
    list_display = ("group", "class_number")


admin.site.register(Student, StudentAdmin)
admin.site.register(Class)
admin.site.register(TypeOfClass)
# Register your models here.
