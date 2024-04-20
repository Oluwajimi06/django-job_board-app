# In views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import JobForm,JobApplicationForm
from .models import Job,JobApplication
from django.contrib import messages

from datetime import datetime
from django.core.exceptions import ValidationError
import logging
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            # Parse the date from the form input
            application_deadline = request.POST.get('application_deadline')
            try:
                # Attempt to parse the date
                parsed_deadline = datetime.strptime(application_deadline, '%Y-%m-%d')
                # Save the form data to create a new job object
                job = form.save(commit=False)
                job.posted_by = request.user
                job.application_deadline = parsed_deadline  # Assign the parsed date
                job.save()
                # Redirect to the success page with a success message
                return redirect('job_post_success')
            except ValueError:
                # Handle invalid date format
                form.add_error('application_deadline', 'Enter a valid date in YYYY-MM-DD format.')
        else:
            # If the form is invalid, print form errors and request.FILES
            print(form.errors)
            print(request.FILES)
    else:
        form = JobForm()
    return render(request, 'job/create_job.html', {'form': form})


def job_post_success(request):
    # Render the job post success page
    return render(request, 'job/job_post_success.html')

# def manage_jobs(request):
#     # Add logic to retrieve and display jobs posted by the current user
#     return render(request, 'manage_jobs.html')
# views.py



def manage_jobs(request):
    # Retrieve jobs posted by the logged-in user
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'job/manage_jobs.html', {'jobs': jobs})



def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('manage_jobs')  # Redirect to the manage jobs page
    else:
        form = JobForm(instance=job)
    return render(request, 'job/job_update.html', {'form': form, 'job': job})




def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('manage_jobs')  # Redirect to the manage jobs page
    return render(request, 'job/job_confirm_delete.html', {'job': job})






def apply_for_job(request, job_id):
    if request.method == 'POST':
        # Retrieve the job object from the database
        job = Job.objects.get(pk=job_id)
        
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        portfolio_website = request.POST.get('portfolio_website')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')

        # Ensure user is authenticated
        if request.user.is_authenticated:
            user = request.user
            # Save the job application
            application = JobApplication(
                job=job,
                user=user,
                name=name,
                email=email,
                portfolio_website=portfolio_website,
                cover_letter=cover_letter,
                resume=resume
            )
            application.save()
            # Redirect to a success page
            return redirect('success_page')  # Assuming 'success_page' is the name of your success page URL pattern
        else:
            # Handle unauthenticated user
            return HttpResponse("Unauthorized", status=401)
    else:
        # Handle GET request
        job = Job.objects.get(pk=job_id)
        return render(request, "job/job-details.html", {'job': job})





def applied_jobs(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve applied job applications for the current user
        user = request.user
        applied_jobs = JobApplication.objects.filter(user=user)

        # Pass the applied job applications data to the template
        context = {
            'applied_jobs': applied_jobs
        }
        return render(request, 'job/applied_jobs.html', context)
    else:
        # Redirect unauthenticated users to login page or handle as needed
        return render(request, 'registration/login.html')  # Assuming you have a login template





def view_applicants(request, job_id):
    # Retrieve the job object from the database
    job = get_object_or_404(Job, pk=job_id)

    # Retrieve all job applications for the given job
    job_applications = JobApplication.objects.filter(job=job)

    # Pass job details and applicants to the template
    return render(request, 'job/view_applicants.html', {'job': job, 'job_applications': job_applications})




def posted_jobs(request):
    # Retrieve all jobs posted by the logged-in employer
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'job/posted_jobs.html', {'jobs': jobs})





def save_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    request.user.saved_jobs.add(job)
    return redirect('save_job_success')

def save_job_success(request):
    return render(request,'job/save_job_success.html')



def saved_jobs(request):
    saved_jobs = request.user.saved_jobs.all()
    return render(request, 'job/saved_jobs.html', {'saved_jobs': saved_jobs})



def remove_saved_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.user.is_authenticated:
        request.user.saved_jobs.remove(job)
    return redirect('saved_jobs')  # Redirect to the saved jobs page









def Job_listings(request):
    # Fetch the list of jobs from the database
    jobs = Job.objects.all()

    # Group jobs by job type
    job_types = Job.JOB_TYPE_CHOICES
    grouped_jobs = {}
    for job_type in job_types:
        grouped_jobs[job_type[0]] = jobs.filter(job_type=job_type[0])

    # Pass the grouped jobs to the template context
    context = {
        'grouped_jobs': grouped_jobs,
        'ptitle': "Job Board - Listings"
    }

    return render(request, "job/job-listings.html", context)




def success_page(request):
    return render(request, 'job/success.html')





def job_category(request, category):
    jobs = Job.objects.filter(category=category)
    context = {
        'category': category,
        'jobs': jobs,
    }
    return render(request, 'sitepages/category_jobs.html', context)

def jobs_category(request, category):
    jobs = Job.objects.filter(category=category)
    context = {
        'category': category,
        'jobs': jobs,
    }
    return render(request, 'job/category-jobs.html', context)

def Jobscategory(request):
    categories = dict(Job.CATEGORY_CHOICES)
    context = {
        'categories': categories,
    }
    return render(request, 'job/category.html', context)








def Job_details(request, job_id):
    # Retrieve the job object from the database based on job_id
    job = get_object_or_404(Job, pk=job_id)
    
    # Instantiate the job application form
    form = JobApplicationForm()
    
    # Pass the job object and form to the template
    data = {
        "ptitle": "Job Board - Job details",
        "job": job,
        "form": form  # Pass the form object to the template
    }

    return render(request, "job/job-details.html", data)





def search_results(request):
    # Get the search parameters from the request
    keyword = request.GET.get('keyword', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')

    # Filter jobs based on the search parameters
    jobs = Job.objects.all()
    if keyword:
        jobs = jobs.filter(job_title__icontains=keyword)
    if category:
        jobs = jobs.filter(category=category)
    if location:
        jobs = jobs.filter(location__icontains=location)

    # Pass the filtered jobs to the template context
    context = {
        'jobs': jobs,
        'keyword': keyword,
        'category': category,
        'location': location,
    }

    return render(request, 'sitepages/search_results.html', context)


def searchresults(request):
    # Get the search parameters from the request
    keyword = request.GET.get('keyword', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')

    # Filter jobs based on the search parameters
    jobs = Job.objects.all()
    if keyword:
        jobs = jobs.filter(job_title__icontains=keyword)
    if category:
        jobs = jobs.filter(category=category)
    if location:
        jobs = jobs.filter(location__icontains=location)

    # Pass the filtered jobs to the template context
    context = {
        'jobs': jobs,
        'keyword': keyword,
        'category': category,
        'location': location,
    }

    return render(request, 'job/search_results.html', context)