from django.db import models

# Create your models here
class Student(models.Model):
    name = models.CharField(max_length=255)
    big_number = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=255)
    email = models.EmailField(max_length=255)
    file = models.FileField(upload_to='')
    image = models.ImageField(upload_to='')
    
