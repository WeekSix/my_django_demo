from django.shortcuts import render

# Create your views here.
from .models import BlogPost

article = BlogPost.objects.get(id=1)


def blog_post_detail_page(request):
    article = BlogPost.objects.get(id=1)  # query -> database -> data -> django render it
    template_name = 'blog_post_detail.html'
    context = {"object": article}
    return render(request, template_name, context)
