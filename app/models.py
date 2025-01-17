from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("is_completed", "-datetime",)

    def __str__(self) -> str:
        return (
            f"{self.content} "
            f"({', '.join([str(tag) for tag in self.tags.all()])})"
        )
