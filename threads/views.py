from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from users.models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404
from django.contrib import messages


# Create your views here.
def index(request):
    threads = Thread.objects.all().order_by("-likes")[:20]
    # threads_text = threads.text
    # threads_group = threads.group
    # threads_image = threads.image
    avatar = User.objects.all()
    return render(
        request,
        "threads/index.html",
        {
            "threads": threads,
            # "threads_text": threads_text,
            # "threads_group": threads_group,
            # "threads_image": threads_image,
            "avatar": avatar,
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
def delete_thread(request, threads_id):

    threads = Thread.objects.get(id=threads_id, user=request.user)
    threads = get_list_or_404(Thread, id=threads_id, user=request.user)
    threads.delete()
    return HttpResponseRedirect(reverse("threads:index"))


@login_required
def like_thread(request, threads_id):
    if Thread.objects.filter(id=threads_id):
        threads = Thread.objects.get(id=threads_id)
        threads.likes += 1
        threads.save()
    # Redirect to index page, but don't reload to the top of the page like normal, stay at current post
    return HttpResponseRedirect(
        reverse("threads:index") + "#threads_id_%s" % (threads.id)
    )


@login_required
def dislike_thread(request, threads_id):
    if Thread.objects.filter(id=threads_id):
        threads = Thread.objects.get(id=threads_id)
        threads.dislikes += 1
        threads.save()
    # Redirect to index page, but don't reload to the top of the page like normal, stay at current post
    return HttpResponseRedirect(
        reverse("threads:index") + "#threads_id_%s" % (threads.id)
    )
