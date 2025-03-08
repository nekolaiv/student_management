from django.db import models

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="students", default=None)
    student_id = models.BigIntegerField(primary_key=True, default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    COURSE_CHOICES = [
        ('cs', 'Computer Science'),
        ('it', 'Information Technology'),
        ('eng', 'Engineering'),
    ]
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    enrollment_date = models.DateField()


    def __str__(self):
        return self.name
