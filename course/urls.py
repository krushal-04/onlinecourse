from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_detail, name='course_detail'),  # 👈 ADD THIS

    path('submit/<int:course_id>/', views.submit, name='submit'),
    path('result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]