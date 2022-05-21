from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, redirect
from django.contrib import messages
from threads.models import *


@login_required
def user_profile(request):
    threads = Thread.objects.filter(user=request.user)
    avatar = User.objects.all()

    return render(request, "users/profile.html", {"threads": threads, "avatar": avatar})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("threads:index"))


def user_register(request):
    if request.method == "GET":
        form = NewRegisterForm()
        return render(request, "users/create_user.html", {"form": form})

    elif request.method == "POST":
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            authenticate(request, user=user, password1=password)
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("threads:index"))
            # else:
            #     form.add_error("username", "Invalid Credentials")
        return render(request, "users/create_user.html", {"form": form})


def user_login(request):

    if request.method == "GET":
        return render(request, "users/login.html", {"form": NewLoginForm()})
    elif request.method == "POST":
        form = NewLoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            user = authenticate(
                request, username=form.cleaned_data["username"], password=password
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("threads:index"))

            else:
                form.add_error("username", "Invalid Credentials")
                return render(request, "users/login.html", {"form": form})


@login_required
def follow_user(request, userID):
    return redirect(request.META["HTTP_REFERER"])


def user_public_profile(request, userID):
    threads = Thread.objects.all()
    public_user = User.objects.all()
    userID = userID
    return render(
        request,
        "users/public_profile.html",
        {"threads": threads, "public_user": public_user, "userID": userID},
    )
