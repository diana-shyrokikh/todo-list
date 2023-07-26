from django.urls import path, include

from todo_list.views import (
    IndexView,

)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

]

app_name = "todo_list"
