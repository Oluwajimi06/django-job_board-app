# In urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('create_job/', views.create_job, name='create_job'),
    path('job_post_success/', views.job_post_success, name='job_post_success'),
    path('manage/', views.manage_jobs, name='manage_jobs'),
    path('job/<int:pk>/update/',views.job_update, name='job_update'),
    path('job/<int:pk>/delete/',views.job_delete, name='job_delete'),
    path('success/', views.success_page, name='success_page'),
    path('apply/<int:job_id>/',views.apply_for_job, name='apply_for_job'),
    path('job/<int:job_id>/applicants/',views.view_applicants, name='view_applicants'),
    path('posted_jobs/', views.posted_jobs, name='posted_jobs'),
    path('save-job/<int:job_id>/', views.save_job, name='save_job'), 
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('saved-job-success/', views.save_job_success, name='save_job_success'),
    path('jobs/remove-saved/<int:job_id>/', views.remove_saved_job, name='remove_saved_job'),
    path('job-category/<str:category>/', views.job_category, name='job_category'),
    path('jobs-categorys/<str:category>/', views.jobs_category, name='jobs_categorys'),
    path('jobs-category/',views.Jobscategory,name="jobs-category"),
    path('search/', views.search_results, name='search_results'),
    path('search-results/', views.searchresults, name='searchs_results'),
    
    # path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('view-applied-jobs/', views.applied_jobs, name='view_applied_jobs'),
    path('view-job-listings/', views.Job_listings, name='view_Job_listings'),
    path('view-job-details/<int:job_id>/', views.Job_details, name='view_Job_details'),  

    # path('manage_jobs/', views.manage_jobs, name='manage_jobs'),
    # Add other URLs as needed
]



