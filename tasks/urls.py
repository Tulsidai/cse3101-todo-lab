from django.urls import path

from . import views

urlpatterns = [
    # Activity 3
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/<int:pk>/", views.task_detail, name="task_detail"),
    # Activity 4
    path('tasks/new/', views.task_create, name="task_create"),
    # Activity 5
    path('tasks/<int:pk>/edit/', views.task_edit, name="task_edit"),
    # Activity 6
    path('tasks/<int:pk>/delete/', views.task_delete, name="task_delete"),
]