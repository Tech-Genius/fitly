from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def community(request):
    threads = Thread.objects.all()
    return render(request, 'thread/community.html', {'threads':threads})


def post_thread(request):
    
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = Thread(user=request.user, title=request.POST['title'], content=request.POST['content'])
            thread.save()
        messages.success(request, f"{request.user.username}, you've successfully created a new thread!")  
        return redirect('community')
    else:
        form = ThreadForm()    
    # threads = Thread.objects.filter(user=request.user)
    context = {'form': form}
    return render(request, 'thread/post_thread.html', context)


def active_thread(request, pk):
    thread = Thread.objects.get(id=pk)
    if request.method == 'POST':
        rf = ReplyForm(request.POST)
        if rf.is_valid():
          content = request.POST.get('content')
          reply = Reply.objects.create(thread = thread, user = request.user, content = content)
          reply.save()
          return redirect('active_thread', pk=thread.id)     
    else:   
        rf = ReplyForm()
    context = {'thread': thread, 'reply_form': rf}
    return render(request, 'thread/active_thread.html', context)
























def delete_thread(request, pk=None):
    Thread.objects.get(id=pk).delete()
    return redirect("community")     
