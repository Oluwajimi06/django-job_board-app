from django.shortcuts import render,redirect,get_object_or_404
from jobs.models import Job
from jobs.forms import JobApplicationForm
from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import ContactMessage

# Create your views here.
def Home(request):
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
        'ptitle': "Job Board - homepage"  # Add page title to the context
    } 

    return render(request, "sitepages/index.html", context)

def About(request):

    data = {"ptitle":"Job Board - About Us"}

    return render(request,"sitepages/about.html",data)


# views.py


def Jobcategory(request):
    categories = dict(Job.CATEGORY_CHOICES)
    context = {
        'categories': categories,
    }
    return render(request, 'sitepages/category.html', context)



def Joblistings(request):
    # Fetch the list of jobs from the database
    jobs = Job.objects.all()

    # Pass the list of jobs to the template context
    context = {
        'jobs': jobs,
        'ptitle': "Job Board - Listings"  # Add page title to the context
    } 

    return render(request, "sitepages/job-list.html", context)








def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  # Retrieve the email entered by the user from the form
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save contact message to the database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email using the email entered by the user as the sender
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,  # Use the email entered by the user as the sender
            [settings.EMAIL_HOST_USER],  # Your email address as the recipient
            fail_silently=False,
        )

        # Render the 'message_success' template directly
        return render(request, 'sitepages/message_success.html', {'ptitle': 'Job Board - Message success', 'name': name})

    else:
        return render(request, "sitepages/contact.html", {'ptitle': 'Job Board - Contact'})




def message_success(request, name):
    data = {
        "ptitle": "Job Board - Message success",
        "name": name
    }
    return render(request, 'sitepages/message_success.html', data)


def Contact(request):

    data = {"ptitle":"Job Board - Contact"}

    return render(request,"sitepages/contact.html",data)

def Testimonial(request):

    data = {"ptitle":"Job Board - Testimonials"}

    return render(request,"sitepages/testimonial.html",data)





def Jobdetails(request, job_id):
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

    return render(request, "sitepages/job-detail.html", data)



def Register(request):

    data = {"ptitle":"Job Board - register/signup"}

    return render(request,"sitepages/register.html",data)