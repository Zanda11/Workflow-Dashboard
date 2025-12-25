from django.urls import path
from .views import (
    my_tasks,
    update_task,
    manager_dashboard,
    export_tasks_excel
)

urlpatterns = [
    path('my-tasks/', my_tasks, name='my_tasks'),
    path('update-task/<int:task_id>/', update_task, name='update_task'),
    path('dashboard/', manager_dashboard, name='dashboard'),
    path('export-excel/', export_tasks_excel, name='export_excel'),
]
