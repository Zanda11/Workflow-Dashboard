from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def kanban_board(request):
    tasks_todo = Task.objects.filter(status='TODO')
    tasks_doing = Task.objects.filter(status='DOING')
    tasks_done = Task.objects.filter(status='DONE')

    return render(request, 'kanban.html', {
        'tasks_todo': tasks_todo,
        'tasks_doing': tasks_doing,
        'tasks_done': tasks_done,
    })


@login_required
def move_task(request, task_id, status):
    task = get_object_or_404(Task, id=task_id)
    task.status = status
    if status == 'DONE':
        task.progress = 100
    task.save()
    return redirect('kanban')
