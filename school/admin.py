from django.contrib import admin
from .models import Student, Class


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "family_name", "birthday", "address")


admin.site.register(Student, StudentAdmin)
# Register your models here.
