from django.db import models

# Create your models here.
class Gender(models.TextChoices):
    MALE = ('M','Male')
    FEMALE = ('F','Female')

class Student(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    gender = models.CharField(choices=Gender.choices)

    class Meta:
        abstract = True
        app_label = 'student_table'
        ordering = ['-created_at']
        get_latest_by = ['-updated_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(gender__in=Gender.values),
                name='valid_gender'
            )
        ] 
