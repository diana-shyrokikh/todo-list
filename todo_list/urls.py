from django.urls import path, include

from todo_list.views import (
    ChangeStatus,
    IndexView,
    TaskCreateView,

)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/<int:pk>/status/",
         ChangeStatus.as_view(),
         name="change-status"
        ),
    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create"
        ),
    # path("tags/create/",
    #      TagCreateView.as_view(),
    #      name="tag-create"
    #     ),



]

app_name = "todo_list"
