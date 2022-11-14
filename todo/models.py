from django.db import models


class Task(models.Model):
    content = models.TextField
    datetime = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(related_name="tasks")

    class Meta:
        ordering = ["datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=100)
