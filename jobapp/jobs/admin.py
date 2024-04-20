from django.contrib import admin
from .models import Job,JobApplication

# Define the admin class for the Job model
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_type', 'posted_by', 'posted_date')
    list_filter = ('job_type', 'posted_date')
    search_fields = ('job_title', 'job_description', 'category')
    date_hierarchy = 'posted_date'

# Register the Job model with the admin site
admin.site.register(Job, JobAdmin)




# Register your models here.
admin.site.register(JobApplication)




