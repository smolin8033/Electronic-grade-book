from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class TypeOfClass(models.Model):
    type_of_class = models.CharField(max_length=50)

    def __str__(self):
        return self.type_of_class

    class Meta:
        verbose_name = "Type of class"
        verbose_name_plural = "Types of classes"


class Class(models.Model):
    group = models.CharField(max_length=30)
    class_number = models.IntegerField()
    type_of_class = models.ForeignKey(TypeOfClass, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s%s" % \
               (self.class_number, self.group)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    birthday = models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT)

    def get_full_name(self):
        return "%s %s %s" % (self.first_name, self.second_name, self.family_name)

    def get_absolute_url(self):
        return reverse("manager_class", kwargs={"pk": self.class_id.id})

    def __str__(self):
        return "%s %s %s, address: %s " % \
               (self.first_name, self.second_name, self.family_name, self.address)

    class Meta:
        ordering = ("family_name",)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    birthday = models.DateField()
    salary = models.CharField(max_length=50)  # add money form
    gender = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s %s" % \
               (self.family_name, self.first_name, self.second_name)

    def get_absolute_url(self):
        return reverse("teacher_list")

    class Meta:
        ordering = ("family_name",)


class Discipline(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default="")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, default="")
    hours = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify("{obj.name}-of-{obj.teacher_id}".format(obj=self))
        super(Discipline, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teacher_list")


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default="")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, default="")
    commentary = models.TextField()
    discipline_id = models.ForeignKey(Discipline, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse("teacher_tasks", kwargs={"pk": self.class_id.id})

    class Meta:
        ordering = ("end_date",)


class Mark(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, default="")
    final_score = models.IntegerField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(self.final_score)

# Create your models here.
