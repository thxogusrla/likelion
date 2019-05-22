from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic. base import TemplateView
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
# Create your views here.
def layout(request):
    return render(request, 'blog/layout.html')

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/home/')


class MainpageView(TemplateView):
    template_name = 'blog/main.html'
    
def detail(request, blog_id, comment=None):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("blog:detail", blog_id)        
    else:
        form = CommentForm(instance=comment)
        return render(request, "blog/detail.html",{"blog":blog, "form":form})

def blogform(request, blog_id=None):
    if request.method =='POST':
        form = BlogForm(request.POST, instance=blog_id)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('blog:home')
    else:
        form = BlogForm(instance=blog_id)
        return render(request, 'blog/new.html', {'form':form})

def edit(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return blogform(request, blog)

def remove(request, blog_id):
    blog =get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog:home')

def edit_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return detail(request, blog_id, comment)

def remove_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('blog:home')
    
