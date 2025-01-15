from django.urls import path

from app.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    ToggleCompleteStatusView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "toggle_complete_status/<int:pk>/",
        ToggleCompleteStatusView.as_view(),
        name="toggle-complete-status"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "app"
