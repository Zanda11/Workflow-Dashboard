from django.urls import path
from . import views

urlpatterns = [
    path('my-tasks/', views.my_tasks, name='my_tasks'),
    path('kanban/', views.kanban_board, name='kanban'),
    path('move-task/<int:task_id>/<str:status>/', views.move_task, name='move_task'),
]
