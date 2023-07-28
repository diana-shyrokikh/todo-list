from django.urls import path

from todo_list.views import (
    ChangeStatus,
    IndexView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/<int:pk>/status/", ChangeStatus.as_view(), name="change-status"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/list/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
