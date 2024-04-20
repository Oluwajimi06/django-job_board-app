from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import User  # Import your custom User model



class Job(models.Model):
    # Job Type Choices
    JOB_TYPE_CHOICES = [
        ('Onsite', 'Onsite'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time'),
        ('Internship', 'Internship'),
    ]

    # Category Choices
    CATEGORY_CHOICES = [
        ('Marketing', 'Marketing'),
        ('Customer Service', 'Customer Service'),
        ('Human Resource', 'Human Resource'),
        ('Project Management', 'Project Management'),
        ('Software Development', 'Software Development'),
        ('Sales & Communication', 'Sales & Communication'),
        ('Teaching & Education', 'Teaching & Education'),
        ('Design & Creative', 'Design & Creative'),
    ]

    company_logo = models.ImageField(upload_to='company_logos/')
    company_name = models.CharField(max_length=100,default='Unknown') 
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary_range = models.CharField(max_length=100)
    application_deadline = models.DateField()
    responsibility = models.TextField()
    qualifications = models.TextField()
    company_details = models.TextField()
    location = models.CharField(max_length=100, default='Unknown')  # New field for location
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)  # Added field for date
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Added field for category
    saved_by = models.ManyToManyField(User, related_name='saved_jobs', blank=True)

    def __str__(self):
        return self.job_title






class JobApplication(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    portfolio_website = models.URLField(blank=True, null=True)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.name} - {self.job.job_title}"



