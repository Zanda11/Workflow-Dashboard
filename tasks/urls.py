from django.urls import path
from . import views

urlpatterns = [
    path("my-tasks/", views.my_tasks, name="my_tasks"),
    path("tasks/<int:task_id>/update/", views.update_task, name="update_task"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("kanban/", views.kanban_board, name="kanban"),
    path("list/", views.task_list, name="task_list"),
]
