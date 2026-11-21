from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import TodoForm
from .models import Todo


# Create your views here.
@require_GET
def home(request):
    return redirect ("task_list")

@require_GET
def task_list(request):
    tasks = Todo.objects.all()
    return render(request, 'tasks/task_list.html', { "tasks":tasks })


@require_GET
def task_detail(request, pk):
    task = get_object_or_404(Todo, pk = pk)
    return render(request,"tasks/task_detail.html", {'task': task})



@require_http_methods(["GET", "POST"])
def task_create(request):
    if request.method == 'POST':
        form = TodoForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect("task_list" )

        # show the form again with the errors
        return render(request, 'tasks/form.html', {"form": form},status=400)
    form = TodoForm()

    return render (request, "tasks/form.html", {'form':form})