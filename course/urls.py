from django.urls import path
from . import views

# This is required for the 'course:' prefix in your redirects and templates
app_name = 'course'

urlpatterns = [
    # Path to see the course details and questions
    path('<int:course_id>/', views.course_details, name='course_details'),
    
    # Task 6 Requirement: Submit path
    path('submit/<int:course_id>/', views.submit, name='submit'),
    
    # Task 6 Requirement: Result path
    path('result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]