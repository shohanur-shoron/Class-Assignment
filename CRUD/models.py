from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50, null=False, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name