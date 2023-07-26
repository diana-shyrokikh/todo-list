from django.urls import path, include

from todo_list.views import (
    ChangeStatus,
    IndexView,

)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/<int:pk>/status/",
         ChangeStatus.as_view(),
         name="change-status"
        ),

]

app_name = "todo_list"
