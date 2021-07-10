from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view),
    path('student/current/', views.student_current),
    path('student/all/', views.student_current),
]