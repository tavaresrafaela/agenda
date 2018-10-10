from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Cadastro
from .forms import PostForm, CadForm
from events.models import Event, Register
from django.utils.timezone import localdate
from datetime import datetime


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }

    return render(request, 'blog/post_edit.html', context)

def day():
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
    }

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }

    return render(request, 'blog/post_edit.html', context)







def cad_list(request):
    cadastros = Cadastro.objects.all()
    return render(request, 'blog/cad_list.html', {'cadastros': cadastros})


def cad_detail(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    return render(request, 'blog/cad_detail.html', {'cadastro': cadastro})


def cad_new(request):
    if request.method == "POST":
        form = CadForm(request.POST)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.save()
            return redirect('cad_detail', pk=cadastro.pk)
    else:
        form = CadForm()
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Cadastro.objects.all(),
        'form': form
    }

    return render(request, 'blog/cad_edit.html', context)

def day():
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Cadastro.objects.all(),
    }

def cad_edit(request, pk):
    cadastro = get_object_or_404(Register, pk=pk)
    if request.method == "REGISTER":
        form = CadForm(request.REGISTER, instance=cadastro)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.save()
            return redirect('cad_detail', pk=cadastro.pk)
    else:
        form = CadForm(instance=cadastro)

    context = {
        'events': Cadastro.objects.all(),
        'form': form
    }

    return render(request, 'blog/cad_edit.html', context)



