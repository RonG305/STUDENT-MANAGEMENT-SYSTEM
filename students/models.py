from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=200)
    gpa = models.FloatField()


    def __str__(self):
        return f'NAME: {self.first_name} {self.last_name}'
    