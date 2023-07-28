from django.contrib import admin

from todo_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_done",
        "created_at",
        "deadline",
    ]
    search_fields = ["name"]
    list_filter = ["tags"]


admin.site.register(Tag)
