from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


class Jobseeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key = True )
    occupation = models.TextField(max_length=100,blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    education = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company_email = models.EmailField(default='')  # Add this field
    contact_phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username



