from django.urls import path
from .views import test_view, student_view

urlpatterns = [
    path('', test_view),
    path('student/', student_view),
]