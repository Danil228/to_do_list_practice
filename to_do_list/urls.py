from django.urls import path

from to_do_list.views import TaskListView, TagListView, TagCreateView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create", TagCreateView.as_view(), name="tag-create"),
]

app_name = "to_do_list"
