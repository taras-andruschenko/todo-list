from django.shortcuts import render

from todo.models import Task, Tag


def index(request):

    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks": tasks,
        "tags": tags,
    }

    return render(request, "todo/index.html", context=context)
