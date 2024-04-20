from django.urls import path
from .views import *
# Create your tests here.


urlpatterns = [
    path('accounts/signup/jobseeker/',JobseekerSignUpView.as_view(),name='jobseeker_signup'),
    path('accounts/signup/employer/',EmployerSignUpView.as_view(),name='employer_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='custom_logout'),
    path('employer/dashboard/', employer_dashboard, name='employer_dashboard'),
    path('jobseeker/dashboard/', jobseeker_dashboard, name='jobseeker_dashboard'),
     path('edit/jobseeker/', edit_jobseeker_profile, name='edit_jobseeker_profile'),
    path('edit/employer/', edit_employer_profile, name='edit_employer_profile'),
]