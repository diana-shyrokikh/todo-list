from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View, generic

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class IndexView(View):

    @staticmethod
    def get(request):

        tasks = Task.objects.prefetch_related("tags")

        context = {
            "tasks": tasks,
        }
        return render(request, "todo_list/index.html", context=context)


class ChangeStatus(View):

    @staticmethod
    def get(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect("todo_list:index")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")
