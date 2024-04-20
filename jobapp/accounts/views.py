from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.conf import settings
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .models import *
from jobs.models import Job


# Create your views here.
class JobseekerSignUpView(CreateView):
    model = Jobseeker  # Use the Jobseeker model
    form_class = JobSeekerSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobseeker'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()

        jobseeker = Jobseeker.objects.create(
            user=user,
            occupation=form.cleaned_data['occupation'],
            resume=form.cleaned_data['resume'],
            education=form.cleaned_data['education'],
            experience=form.cleaned_data['experience'],
            skills=form.cleaned_data['skills']
        )
        
        return redirect(self.success_url)


class EmployerSignUpView(CreateView):
    model = Employer
    form_class = EmployerSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  # Redirect to login

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        employer = Employer.objects.create(
            user=user,
            company_name=form.cleaned_data['company_name'],
            industry=form.cleaned_data['industry'],
            location=form.cleaned_data['location'],
            contact_phone=form.cleaned_data['contact_phone'],
            company_email=form.cleaned_data['company_email'],
            website=form.cleaned_data['website']
        )

        return redirect(self.success_url)










class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_jobseeker:
                return reverse_lazy('jobseeker_dashboard')
            elif user.is_employer:
                return reverse_lazy('employer_dashboard')

        # If user type is not recognized or user is not authenticated, return to home page
        return reverse_lazy('/')  # Replace 'home' with the name of your home page URL pattern






@login_required
def employer_dashboard(request):
    # Add any logic or data retrieval specific to the employer dashboard
    return render(request, 'sitepages/employer_dashboard.html')

@login_required
def jobseeker_dashboard(request):
    jobs = Job.objects.all()
    categories = dict(Job.CATEGORY_CHOICES)
    

    # Group jobs by job type
    job_types = Job.JOB_TYPE_CHOICES
    grouped_jobs = {}
    for job_type in job_types:
        grouped_jobs[job_type[0]] = jobs.filter(job_type=job_type[0])

   

    # Pass the list of jobs to the template context
    context = {
        'jobs': jobs,
        'grouped_jobs': grouped_jobs,
        'categories': categories,
        'ptitle': "Job Board - Jobseeker Dashboard"  # Add page title to the context
    } 

    
    # Add any logic or data retrieval specific to the jobseeker dashboard
    return render(request, 'sitepages/jobseeker_dashboard.html',context)


def custom_logout(request):
    logout(request)
    # Redirect to your home page or any other desired URL after logout
    return redirect('/')





def edit_jobseeker_profile(request):
    jobseeker = Jobseeker.objects.get(user=request.user)
    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST, instance=jobseeker)
        if form.is_valid():
            form.save()
            return redirect('edit_jobseeker_profile')  # Redirect to profile view page
    else:
        form = JobSeekerProfileForm(instance=jobseeker)
    return render(request, 'profile/edit_jobseeker_profile.html', {'form': form})

def edit_employer_profile(request):
    employer = Employer.objects.get(user=request.user)
    if request.method == 'POST':
        form = EmployerProfileForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            return redirect('edit_employer_profile')  # Redirect to profile view page
    else:
        form = EmployerProfileForm(instance=employer)
    return render(request, 'profile/edit_employer_profile.html', {'form': form})
