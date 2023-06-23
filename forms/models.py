from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.full_name
