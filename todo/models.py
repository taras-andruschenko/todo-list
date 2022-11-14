from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    content = models.TextField(default="Please, fill me in")
    datetime = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", )

    class Meta:
        ordering = ["deadline", "status"]
