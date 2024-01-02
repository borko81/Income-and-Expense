from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def base(request):
    context = {"title": "title"}
    return render(request, "base.html", context=context)
