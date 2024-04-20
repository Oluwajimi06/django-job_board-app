from django.urls import path
from .views import *
app_name="sitepages"

urlpatterns = [
    path('',Home,name="homepage"),
    path('about/',About,name="about"),
    path('job-category/',Jobcategory,name="category"),
    path('job-listing/',Joblistings,name="listing"),
    path('job/<int:job_id>/', Jobdetails, name='job_details'),
    path('contact/',Contact,name="contact"),
    path('submit/', contact_submit, name='contact_submit'),
    path('message-success/<str:name>/', message_success, name='message_success'),
    path('testimonial/',Testimonial,name="testimonial"),
    path('register/',Register,name="register"),
]