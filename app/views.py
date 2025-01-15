from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views import generic

from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline_datetime", "tags",)
    success_url = reverse_lazy("app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline_datetime", "is_completed", "tags",)
    success_url = reverse_lazy("app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")


class ToggleCompleteStatusView(generic.View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        task = Task.objects.get(pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect(reverse("app:task-list"))
