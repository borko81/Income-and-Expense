from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . import forms
from . import models


def login_user(request):
    return render(request, "registration/login.html")


def logout_user(request):
    pass


@login_required
def show_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    try:
        user_profile = models.UserProfile.objects.get(user_id=user.id)
        form = forms.ProfileForm(request.POST or None, instance=user_profile or None)
        content = {"title": "ProfilePage", "user": user, "user_profile": user_profile}
    except:
        form = forms.ProfileForm(request.POST)
        content = {"title": "ProfilePage", "user": user, "user_profile": None}

    if request.GET.get("edit"):
        content.update({"form": form})

    if request.method == "POST":
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = user
            f.save()
            content.update(
                {"user_profile": models.UserProfile.objects.get(user_id=user.id)}
            )
    return render(request, "user_profile/profile.html", content)


@login_required
def delete_profile(request, id_):
    user_profile = get_object_or_404(models.UserProfile, user_id=id_)
    user_profile.delete()
    return redirect("base")


@login_required
def send_message(request, id_):
    pass
