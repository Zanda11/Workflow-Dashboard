from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, "tasks/my_tasks.html", {"tasks": tasks})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.status = request.POST.get("status")
        task.progress = request.POST.get("progress")
        task.save()
        return redirect("my_tasks")

    return render(request, "tasks/update_task.html", {"task": task})


@login_required
def dashboard(request):
    total = Task.objects.count()
    done = Task.objects.filter(status="DONE").count()

    progress = 0
    if total > 0:
        progress = int((done / total) * 100)

    return render(request, "tasks/dashboard.html", {
        "total": total,
        "done": done,
        "progress": progress,
    })


@login_required
def kanban_board(request):
    tasks_todo = Task.objects.filter(status='TODO')
    tasks_doing = Task.objects.filter(status='DOING')
    tasks_done = Task.objects.filter(status='DONE')

    return render(request, "tasks/kanban.html", {
        "tasks_todo": tasks_todo,
        "tasks_doing": tasks_doing,
        "tasks_done": tasks_done,
    })


