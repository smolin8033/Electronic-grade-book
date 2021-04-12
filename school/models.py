from django.db import models


class TypeOfClass(models.Model):
    type_of_class = models.CharField(max_length=50)

    def __str__(self):
        return self.type_of_class


class Class(models.Model):
    group = models.CharField(max_length=30)
    class_number = models.IntegerField()
    type_of_class = models.ForeignKey(TypeOfClass, on_delete=models.DO_NOTHING, default="")

    def __str__(self):
        return "%s%s" % \
               (self.class_number, self.group)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    birthday = models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING, default="")

    def get_full_name(self):
        return "%s %s %s" % (self.first_name, self.second_name, self.family_name)

    def __str__(self):
        return "%s %s %s, address: %s " % \
               (self.first_name, self.second_name, self.family_name, self.address)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    birthday = models.DateField()
    salary = models.CharField(max_length=50)  # add money form
    gender = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s" % \
               (self.family_name, self.first_name, self.second_name)


class Discipline(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING, default="")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, default="")
    hours = models.IntegerField()

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING, default="")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, default="")
    commentary = models.TextField()
    discipline_id = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, default="")


class Curriculum(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, default="")
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING, default="")
    discipline_id = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, default="")


class Mark(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING, default="")
    final_score = models.IntegerField()
    task_id = models.ForeignKey(Task, on_delete=models.DO_NOTHING, default="")


# Create your models here.
