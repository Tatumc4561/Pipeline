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


def user_profile(request, userID):
    threads = Thread.objects.all()
    public_user = User.objects.all()
    userID = userID
    search = Channel.objects.all().order_by("-name")

    return render(
        request,
        "users/profile.html",
        {
            "threads": threads,
            "public_user": public_user,
            "userID": userID,
            "search": search,
        },
    )


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

    search = Channel.objects.all().order_by("-name")

    if request.method == "GET":
        return render(
            request, "users/login.html", {"form": NewLoginForm(), "search": search}
        )
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


# @login_required
# def follow_user(request, userID):
#     follow_user = User.objects.get(username=userID)
#     MyFollowings.set(user=follow_user, follower=request.user, following=follow_user)
#     return redirect(request.META["HTTP_REFERER"])


@login_required
def follow_user(request, userID):
    follow = User.objects.get(username=userID)
    Following.objects.create(user_follower=request.user, target_following=follow)
    # MyFollowings.set(user=follow_user, follower=request.user, following=follow_user)
    return redirect(request.META["HTTP_REFERER"])


def user_public_profile(request, userID):
    threads = Thread.objects.all()
    public_user = User.objects.all()
    userID = userID
    search = Channel.objects.all().order_by("-name")

    return render(
        request,
        "users/public_profile.html",
        {
            "threads": threads,
            "public_user": public_user,
            "userID": userID,
            "search": search,
        },
    )


def group_page(request, groupID):
    group = Channel.objects.get(id=groupID)
    threads = Thread.objects.all().filter(group=group)
    search = Channel.objects.all().order_by("-name")

    return render(
        request,
        "users/group.html",
        {
            "threads": threads,
            "group": group,
            "search": search,
        },
    )


@login_required
def group_register(request):
    search = Channel.objects.all().order_by("-name")

    if request.method == "GET":
        return render(request, "users/create_group.html", {"search": search})

    elif request.method == "POST":
        name = request.POST.get("group_name")
        Channel.objects.create(
            name=request.POST.get("group_name"), avatar=request.FILES.get("avatar")
        )
        JoinGroup.objects.create(
            join_group=request.user, target_group=Channel.objects.get(name=name)
        )

        return HttpResponseRedirect(reverse("threads:index"))


@login_required
def join_group(request, groupID):
    join = Channel.objects.get(id=groupID)
    JoinGroup.objects.create(join_group=request.user, target_group=join)
    return HttpResponseRedirect(reverse("threads:index"))
