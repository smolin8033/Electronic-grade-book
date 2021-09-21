from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student/unrated/', views.student_unrated, name='student_unrated'),
    path('student/rated/', views.student_rated, name='student_rated'),
    path('teacher/', views.teacher_interface, name='teacher_interface'),
    path('teacher/<int:pk>/class/', views.class_students, name="class_students"),
    path('<int:pk>/class/rated/', views.rated, name="rated"),
    path('<int:pk>/class/all_rated/', views.all_rated, name="all_rated"),
    path('<int:pk>/class/unrated/', views.teacher_unrated, name="teacher_unrated"),
    path('<int:pk>/class/all_unrated/', views.all_unrated, name="all_unrated"),
    path('teacher/<int:pk>/<int:rel_task>/mark/add/', views.mark_create_view, name="mark_add"),
    path('teacher/<int:pk>/mark/update/', views.MarkUpdateView.as_view(), name="mark_update"),
    path('teacher/<int:pk>/mark/delete/', views.MarkDeleteView.as_view(), name="mark_delete"),
    path('teacher/<int:pk>/tasks/', views.TaskListView.as_view(), name="teacher_tasks"),
    path('teacher/<int:pk>/tasks/create/', views.TaskCreateView.as_view(), name="tasks_create"),
    path('teacher/<int:pk>/tasks/update/', views.TaskUpdateView.as_view(), name="tasks_update"),
    path('teacher/<int:pk>/tasks/delete/', views.TaskDeleteView.as_view(), name="tasks_delete"),
    path('manager/', views.manager_interface, name='manager_interface'),
    path('manager/students/', views.StudentListView.as_view(), name="student_list"),
    path('manager/teachers/', views.TeacherListView.as_view(), name="teacher_list"),
    path('manager/discipline/create/', views.DisciplineCreateView.as_view(), name="discipline_create"),
    path('manager/discipline/<slug:slug>/update/', views.DisciplineUpdateView.as_view(), name="discipline_update"),
    path('manager/discipline/<slug:slug>/delete/', views.DisciplineDeleteView.as_view(), name="discipline_delete"),
    path('manager/teachers/create/', views.TeacherCreateView.as_view(), name="teacher_create"),
    path('manager/teachers/<int:pk>/update/', views.TeacherUpdateView.as_view(), name="teacher_update"),
    path('manager/teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name="teacher_delete"),
    path('manager/choice/', views.manager_choice, name="manager_choice"),
    path('manager/<int:pk>/class/', views.manager_class, name="manager_class"),
    path('manager/<int:pk>/class/new-student/', views.StudentCreateView.as_view(), name="student_create"),
    path('manager/<int:pk>/class/delete-student/', views.StudentDeleteView.as_view(), name="student_delete"),
]
