from django.shortcuts import render, redirect
from blogs.models import BlogPost
from blogs.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def check_object_owner(request, item):
    """check the item belongs to the login user"""
    if request.user != item.owner:
        raise Http404

# Create your views here.
@login_required
def posts(request):
    """show the all of posts"""

    posts = BlogPost.objects.filter(owner=request.user).order_by('-timestamp')
    context = {
        'posts': posts
    }

    return render(request, 'blogs/posts.html', context)

@login_required
def post(request, post_id):
    """show the detail of post"""
    post = BlogPost.objects.get(id=post_id)
    check_object_owner(request, post)
    context = {
        'post': post
    }
    return render(request, 'blogs/post.html', context)

@login_required
def edit_post(request, post_id):
    """show the detail of post"""
    post = BlogPost.objects.get(id=post_id)
    check_object_owner(request, post)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post.id)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blogs/edit_post.html', context)

@login_required
def add_post(request):
    """show the detail of post"""

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')
    context = {
        'form': form,
    }
    return render(request, 'blogs/add_post.html', context)
