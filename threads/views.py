import re
from tokenize import group
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
    search = Channel.objects.all().order_by("-name")

    all_users = User.objects.all()
    return render(
        request,
        "threads/index.html",
        {
            "threads": threads,
            "all_users": all_users,
            "search": search,
        },
    )


def read_thread(request, thread_id):
    # display particular thread
    read_thread = Thread.objects.filter(id=thread_id)
    # display all profiles
    all_users = User.objects.all()

    # get api readable object id
    parent_threads = Thread.objects.get(id=thread_id)

    # Get First Comments aka Roots of each tree within the the thread
    # tree = Thread.get_annotated_list()
    # tree = Thread.get_tree()
    tree = Thread.objects.order_by("-likes")
    roots = Thread.get_annotated_list(parent=parent_threads)

    # roots = []
    # for each in tree:
    #     if each.id == parent_threads:
    #         x = Thread.get_annotated_list(parent=each)
    #         roots.append(x)
    # temp = []
    # wtf = []

    # for all in tree:
    #     if all.parent_thread == parent_threads:
    #         y = Thread.dump_bulk(parent=all)
    #         temp.append(y)

    # seen = set()
    # treez = []
    # for d in temp:
    #     for branch in d:
    #         t = tuple(branch)
    #         if t not in seen:
    #             seen.add(t)
    #             treez.append(branch)

    groups = Channel.objects.all()
    search = Channel.objects.all().order_by("-name")

    return render(
        request,
        "threads/thread.html",
        {
            "read_thread": read_thread,
            "all_users": all_users,
            "roots": roots,
            "search": search,
        },
    )


@login_required
def create_thread(request):
    all_users = User.objects.all()
    user = User.objects.all().filter(username=request.user)
    groups = Channel.objects.all()
    search = Channel.objects.all().order_by("-name")

    return render(
        request,
        "threads/create_post.html",
        {
            "form": NewThreadForm(),
            "all_users": all_users,
            "groups": groups,
            "search": search,
        },
    )


@login_required
def submit_thread(request):

    if request.method == "POST":
        form = NewThreadForm(request.POST, request.FILES)
        if form.is_valid():
            # group = request.POST.get("group")
            group = form.cleaned_data["group"]
            title = request.POST.get("title")
            text = request.POST.get("text")
            image = request.FILES.get("image")

            Thread.add_root(
                user=request.user, group=group, title=title, text=text, image=image
            )

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
    return HttpResponseRedirect(
        reverse("threads:index") + "#threads_id_%s" % (threads.id)
    )


@login_required
def dislike_thread(request, thread_id):
    if Thread.objects.filter(id=thread_id):
        threads = Thread.objects.get(id=thread_id)
        threads.likes -= 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return HttpResponseRedirect(
        reverse("threads:index") + "#threads_id_%s" % (threads.id)
    )


@login_required
def comment_thread(request, thread_id):
    x = Thread.objects.get(path=thread_id)

    if request.method == "POST":
        text = request.POST.get("text")
        # if text == "":
        #     return redirect(request.META["HTTP_REFERER"])

        Thread.add_root(user=request.user, text=text, parent_thread=x)

    return redirect(request.META["HTTP_REFERER"])


@login_required
def comment_thread_child(request, thread_id):
    x = Thread.objects.get(path=thread_id)
    y = Thread.objects.get(path=thread_id)

    if request.method == "POST":

        text = request.POST.get("text")
        # if text == "":
        #     return redirect(request.META["HTTP_REFERER"])

        y.add_child(user=request.user, text=text, group=y.group)

    # if NodeAlreadySaved Thread.addSibling()
    return redirect(request.META["HTTP_REFERER"])


@login_required
def like_comment(request, item_id):
    if Thread.objects.filter(id=item_id):
        threads = Thread.objects.get(id=item_id)
        threads.likes += 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return redirect(request.META["HTTP_REFERER"])


@login_required
def dislike_comment(request, item_id):
    if Thread.objects.filter(id=item_id):
        threads = Thread.objects.get(id=item_id)
        threads.likes -= 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return redirect(request.META["HTTP_REFERER"])
    # return redirect(request.META["HTTP_REFERER"]) + "#threads_id_%s" % (threads.id)
    # )
