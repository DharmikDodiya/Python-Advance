from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import PostForm
from .forms import RegisterForm
from django.contrib.auth import login

def home(request):
    posts = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')
    return render(request, 'blog/post_form.html', {'form': form, 'form_title': 'Create Post'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if post.author != request.user:
        return redirect('home')
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/post_form.html', {'form': form, 'form_title': 'Edit Post'})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('home')  # or any page you want
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})