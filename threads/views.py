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

    # get api readable object id
    parent_threads = Thread.objects.get(id=thread_id)

    # Get First Comments aka Roots of each tree within the the thread
    # tree = ThreadComment.get_annotated_list()
    # tree = ThreadComment.get_tree()
    tree = ThreadComment.objects.order_by("-likes")
    roots = []
    for each in tree:
        if each.parent_thread == parent_threads:
            x = ThreadComment.get_annotated_list(parent=each)
            roots.append(x)

    return render(
        request,
        "threads/thread.html",
        {
            "read_thread": read_thread,
            "all_users": all_users,
            "roots": roots,
            "tree": tree,
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
    x = Thread.objects.get(id=thread_id)
    # get = lambda parent_thread: ThreadComment.objects.get(parent_thread=x)

    ThreadComment.add_root(user=request.user, text="lklkhj", parent_thread=x)

    return redirect(request.META["HTTP_REFERER"])


@login_required
def comment_thread_child(request, thread_id):
    x = Thread.objects.get(id=thread_id)

    y = ThreadComment.objects.get(path="0002000100010001")
    y.add_sibling(user=request.user, text="child2text", parent_thread=x)

    # if NodeAlreadySaved ThreadComment.addSibling()
    return redirect(request.META["HTTP_REFERER"])


@login_required
def like_comment(request, item_id):
    if ThreadComment.objects.filter(id=item_id):
        threads = ThreadComment.objects.get(id=item_id)
        threads.likes += 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return redirect(request.META["HTTP_REFERER"])


@login_required
def dislike_comment(request, item_id):
    if ThreadComment.objects.filter(id=item_id):
        threads = ThreadComment.objects.get(id=item_id)
        threads.likes -= 1
        threads.save()
    # Redirect to previous page, and stay at current post
    return redirect(request.META["HTTP_REFERER"])
    # return redirect(request.META["HTTP_REFERER"]) + "#threads_id_%s" % (threads.id)
    # )
