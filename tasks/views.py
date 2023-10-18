from django.shortcuts import render, redirect
from .models import Task




def task_list(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(pk=task_id)
        task.toggle_completion()

    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def toggle_task_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
