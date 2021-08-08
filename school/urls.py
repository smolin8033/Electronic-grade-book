from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='test_view'),
    path('student/current/', views.student_current, name='student_current'),
    path('student/all/', views.student_all, name='student_all'),
    path('teacher/', views.teacher_interface, name='teacher_interface'),
    path('teacher/<int:pk>/class/', views.class_students, name="class_students"),
    path('teacher/<int:pk>/current/', views.teacher_student_current, name="teacher_current"),
    path('teacher/mark/add/', views.mark_create_view, name="mark_add"),
]