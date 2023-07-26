from django.db import models


class Task(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to="Tag",
        related_name="tasks",
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["is_done", "-created_at"]

    def __str__(self):
        return f"{self.name} ({self.is_done})"


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name
