# your_app/templatetags/job_count.py

from django import template
from jobs.models import Job

register = template.Library()

@register.filter
def job_count(category):
    return Job.objects.filter(category=category).count()
