from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from users.models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    threads = Thread.objects.all().order_by("-likes")  # [:20]
    all_users = User.objects.all()
    return render(
        request,
        "threads/index.html",
        {
            "threads": threads,
            "all_users": all_users,
        },
    )


def read_thread(request, thread_id):
    # display particular thread
    read_thread = Thread.objects.filter(id=thread_id)
    # display all profiles
    all_users = User.objects.all()

    parent_thread = Thread.objects.get(id=thread_id)
    # get = ThreadComment.objects.get(parent_thread=parent_thread)

    # tree = ThreadComment.get_tree(parent=get)

    return render(
        request,
        "threads/thread.html",
        {
            "read_thread": read_thread,
            "all_users": all_users,
            # "tree": tree,
            # "get": get,
        },
    )


@login_required
def create_thread(request):
    return render(
        request,
        "threads/create_post.html",
        {"form": NewThreadForm()},
    )


@login_required
def submit_thread(request):
    if request.method == "POST":
        form = NewThreadForm(request.POST, request.FILES)
        if form.is_valid():

            create = form.save(commit=False)
            create.user = request.user
            form.save()

    return HttpResponseRedirect(reverse("threads:index"))


@login_required
def delete_thread(request, thread_id):

    threads = Thread.objects.get(id=thread_id, user=request.user)
    threads = get_list_or_404(Thread, id=thread_id, user=request.user)
    threads.delete()
    return HttpResponseRedirect(reverse("threads:index"))


@login_required
def like_thread(request, thread_id):
    if Thread.objects.filter(id=thread_id):
        threads = Thread.objects.get(id=thread_id)
        threads.likes += 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return redirect(request.META["HTTP_REFERER"])


@login_required
def dislike_thread(request, thread_id):
    if Thread.objects.filter(id=thread_id):
        threads = Thread.objects.get(id=thread_id)
        threads.likes -= 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return redirect(request.META["HTTP_REFERER"])


@login_required
def comment_thread(request, thread_id):
    x = Thread.objects.get(id=thread_id)
    # get = lambda parent_thread: ThreadComment.objects.get(parent_thread=x)

    ThreadComment.add_root(user=request.user, text="lklkhj", parent_thread=x)

    return redirect(request.META["HTTP_REFERER"])


@login_required
def comment_thread_child(request, thread_id):
    x = Thread.objects.get(id=thread_id)

    y = ThreadComment.objects.get(path="000100020001")
    y.add_sibling(user=request.user, text="childtext", parent_thread=x)

    # if NodeAlreadySaved ThreadComment.addSibling()
    return redirect(request.META["HTTP_REFERER"])
