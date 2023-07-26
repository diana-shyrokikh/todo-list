from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from todo_list.models import Task


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
        tasks = Task.objects.prefetch_related("tags")
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done

        task.save()

        context = {
            "tasks": tasks,
        }

        return render(request, "todo_list/index.html", context)



