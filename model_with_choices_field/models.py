from django.db import models

# Create your models here.
class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = ('M','Male')
        FEMALE = ('F','Female')

    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    gender = models.CharField(choices=Gender.choices, max_length=255)

    def __str__(self):
        return self.name
