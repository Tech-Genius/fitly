from django.shortcuts import render,redirect
from . models import *
from . forms import CommentForm
# from account import forms

# Create your views here.




def blog_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_post.html', {'posts' : posts})



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
          content = request.POST.get('content')
          comment = Comment.objects.create(post = post, user = request.user, content = content)
          comment.save()
          return redirect('post_detail', slug=post.slug)
    else:   
        cf = CommentForm()
    return render(request, 'blog/post_detail.html', {'post' : post, 'comment_form':cf})


