from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from .models import Todo


# Create your views here.
@require_GET
def home(request):
    return redirect("task_list")


@require_GET
def task_list(request):
    tasks = Todo.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@require_GET
def task_detail(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})