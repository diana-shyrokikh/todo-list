from django.urls import path, include

from todo_list.views import (
    ChangeStatus,
    IndexView,
    TagCreateView,
    TagUpdateView,
    TaskCreateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "tasks/<int:pk>/status/",
        ChangeStatus.as_view(),
        name="change-status"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),



]

app_name = "todo_list"
