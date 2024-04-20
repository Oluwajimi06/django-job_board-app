from django import forms
from .models import Job
from django.core.exceptions import ValidationError


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_logo','company_name','job_title', 'job_description', 'job_type', 'salary_range', 'application_deadline', 'responsibility', 'qualifications', 'company_details', 'category', 'location']
        labels = {
            'company_logo': 'Company Logo',
            'company_name': 'Company Name',
            'job_title': 'Job Title',
            'job_description': 'Job Description',
            'job_type': 'Job Type',
            'salary_range': 'Salary Range',
            'application_deadline': 'Application Deadline',
            'responsibility': 'Responsibility',
            'qualifications': 'Qualifications',
            'company_details': 'Company Details',
            'category': 'Category',
            'location': 'Location',  # Label for the location field
        }
        widgets = {
            'application_deadline': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
        error_messages = {
            'application_deadline': {
                'invalid': 'Enter a valid date in YYYY-MM-DD format.',
            },
        }










class JobApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    portfolio_website = forms.URLField(required=False)
    cover_letter = forms.CharField(widget=forms.Textarea)
    resume = forms.FileField()

    def clean_resume(self):
        """
        Custom validation for the resume field.
        Ensure that the uploaded file is of an allowed file type (e.g., PDF, DOCX).
        """
        resume = self.cleaned_data.get('resume')

        if not resume:
            raise forms.ValidationError("No file was uploaded.")

        # Add your validation logic here
        # Example: Check file extension
        allowed_extensions = ['pdf', 'docx']
        file_extension = resume.name.split('.')[-1].lower()
        if file_extension not in allowed_extensions:
            raise forms.ValidationError(f"Unsupported file extension. Allowed extensions are: {', '.join(allowed_extensions)}.")

        # Example: Check file size
        max_size = 10 * 1024 * 1024  # 10 MB
        if resume.size > max_size:
            raise forms.ValidationError(f"File size exceeds the maximum limit of 10MB.")

        return resume



