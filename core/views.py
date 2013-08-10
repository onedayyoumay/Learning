# Create your views here.
from models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.comments.models import Comment
from django.core.context_processors import csrf
from django.template import RequestContext

def index(request):
    return render_to_response('base.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('view_post.html', {'categories': Category.objects.all(),
        'posts': Blog.objects.all(),
        'post': get_object_or_404(Blog, slug=slug)
    },  context_instance=RequestContext(request))

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': Category.objects.all(),
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })