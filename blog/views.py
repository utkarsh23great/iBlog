from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
from django.views.generic import View
from django.shortcuts import redirect
from .forms import Addblog

# Create your views here.
def index(request):
    return render(request,'blog/home.html')

def blog(request):
    myposts=Blogpost.objects.all()
    return render(request,'blog/blogs.html',{'mypost':myposts})

def blogpost(request, id):
    post=Blogpost.objects.filter(post_id=id)[0]
    return render(request,'blog/blogpost.html',{'posts':post})

def home(request):
    return render(request,'blog/home.html')

class AddBlog(View):
    def get(self,request):
        form=Addblog(None)
        return render(request,'blog/addblog.html',{'f':form})
    def post(self,request):
        form=Addblog(request.POST,request.FILES)
        form.save()
        return redirect('/blogs/')

def search(request):
    query=request.GET.get('search')
    if query:
        match=Blogpost.objects.filter(title__startswith=query)
        return render(request,'blog/blogs.html',{'mypost':match})