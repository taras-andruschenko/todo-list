from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(default="Please, fill me in")
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", )

    class Meta:
        ordering = ["deadline", "status"]
