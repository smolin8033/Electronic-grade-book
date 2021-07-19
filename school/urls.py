from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='test_view'),
    path('student/current/', views.student_current, name='student_current'),
    path('student/all/', views.student_all, name='student_all'),
    path('teacher/', views.teacher_interface, name='teacher_interface'),
    path('teacher/<int:pk>/class/', views.class_students, name="class_students"),
]