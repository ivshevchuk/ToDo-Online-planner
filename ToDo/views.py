from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


def task_list(request):
    tasks = Task.objects.filter(due_date__gte=timezone.now()).order_by('due_date')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_date = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})


def task_update(request, pk):
    # отримати задачу, яку необхідно оновити, або повернути 404, якщо не існує
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # заповнити форму задачі з даними, що відправлені з форми
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # зберегти оновлену задачу
            form.save()
            return redirect('task_detail', pk=pk)
    else:
        # створити форму з даними про задачу, яку необхідно оновити
        form = TaskForm(instance=task)

    # повернути HTML-сторінку з формою оновлення задачі
    return render(request, 'task_form.html', {'form': form})

def task_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def home(request):
    return render(request, 'home.html')


def task_confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_confirm_delete.html'
