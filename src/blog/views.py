from django.shortcuts import render

# Create your views here.
from .models import BlogPost
from .models import Comment

# article = BlogPost.objects.get(id=1)


def blog_post_detail_page(request):
    article = BlogPost.objects.get(id=1)  # query -> database -> data -> django render it
    comments = []
    for _ in range(1,3):
        comments.append(Comment.objects.get(id=_))
    template_name = 'blog_post_detail.html'
    context = {"object": article, "comments_list": comments}
    return render(request, template_name, context)
