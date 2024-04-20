from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

EDUCATION_CHOICES = [
    ('High School', 'High School'),
    ('Associate Degree', 'Associate Degree'),
    ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
    ('Master\'s Degree', 'Master\'s Degree'),
    ('Ph.D.', 'Ph.D.'),
]

EXPERIENCE_CHOICES = [
    ('Less than 1 year', 'Less than 1 year'),
    ('1-2 years', '1-2 years'),
    ('3-5 years', '3-5 years'),
    ('5-10 years', '5-10 years'),
    ('More than 10 years', 'More than 10 years'),
]

class JobSeekerSignUpForm(UserCreationForm):
    occupation = forms.CharField(max_length=100, required=True)
    resume = forms.FileField(required=True)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=True)
    experience = forms.ChoiceField(choices=EXPERIENCE_CHOICES, required=True)
    skills = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'occupation', 'resume', 'education', 'experience', 'skills']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.occupation = self.cleaned_data.get('occupation')
        user.resume = self.cleaned_data.get('resume')
        user.education = self.cleaned_data.get('education')
        user.experience = self.cleaned_data.get('experience')
        user.skills = self.cleaned_data.get('skills')
        user.is_jobseeker = True

        user.save()
        

        return user



class EmployerSignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=500, required=True)
    industry = forms.CharField(max_length=100, required=True)
    location = forms.CharField(max_length=100, required=True)
    contact_phone = forms.CharField(max_length=20, required=True)
    company_email = forms.EmailField(required=True)
    website = forms.URLField(required=True)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'industry', 'location', 'contact_phone','company_email', 'website']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.company_name = self.cleaned_data.get('company_name')
        user.industry= self.cleaned_data.get('industry')
        user.location = self.cleaned_data.get('location')
        user.contact_phone = self.cleaned_data.get('contact_phone')
        user.company_email = self.cleaned_data.get('company_email')
        user.website = self.cleaned_data.get('website')
        user.is_employer = True

        user.save()
        

        return user







class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['occupation', 'resume', 'education', 'experience', 'skills']

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'industry', 'location', 'contact_phone', 'company_email', 'website']
