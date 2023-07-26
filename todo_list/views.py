from django.shortcuts import render
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


