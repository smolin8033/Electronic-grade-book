from django.urls import path
from . import views
urlpatterns = [
    path('', views.test_view, name='test_view'),
    path('student/current/', views.student_current, name='student_current'),
    path('student/all/', views.student_all, name='student_all'),
    path('teacher/', views.teacher_interface, name='teacher_interface'),
    path('teacher/<int:pk>/class/', views.class_students, name="class_students"),
    path('teacher/<int:pk>/rated/', views.teacher_rated, name="teacher_rated"),
    path('teacher/<int:pk>/all_rated/', views.teacher_all_rated, name="teacher_all_rated"),
    path('teacher/<int:pk>/unrated/', views.teacher_unrated, name="teacher_unrated"),
    path('teacher/<int:pk>/all_unrated/', views.teacher_all_unrated, name="teacher_all_unrated"),
    path('teacher/<int:pk>/<int:rel_task>/mark/add/', views.mark_create_view, name="mark_add"),
    path('teacher/<int:pk>/mark/update/', views.MarkUpdateView.as_view(), name="mark_update"),
    path('teacher/<int:pk>/mark/delete/', views.MarkDeleteView.as_view(), name="mark_delete"),
    path('teacher/<int:pk>/tasks/', views.TaskListView.as_view(), name="teacher_tasks"),
    path('teacher/<int:pk>/tasks/create/', views.TaskCreateView.as_view(), name="tasks_create"),
    path('teacher/<int:pk>/tasks/update/', views.TaskUpdateView.as_view(), name="tasks_update"),
    path('teacher/<int:pk>/tasks/delete/', views.TaskDeleteView.as_view(), name="tasks_delete"),
    path('manager/', views.manager_interface, name='manager_interface'),
]
