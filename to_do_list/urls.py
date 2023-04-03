from django.urls import path

from to_do_list.views import TaskListView, TagListView, TagCreateView, TaskCreateView, TagUpdateView, TaskUpdateView, \
    TagDeleteView, TaskDeleteView, task_completion_confirmation

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/confirm_task", task_completion_confirmation, name="task-confirm"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "to_do_list"
