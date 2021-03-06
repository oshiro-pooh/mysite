from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    posts = Post.objects.all()
    form = PostForm()
    context = {'posts': posts, 'form': form, }
    return render(request, 'todo/index.html', context)
    
@login_required
def create(request):
    form = PostForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('todo:index'))

@login_required
def delete(request, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('todo:index'))