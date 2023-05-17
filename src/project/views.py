from django.shortcuts import render
from django.http import Http404

from .models import ProjectPost

# Create your views here.
def project_post_page(request, post_id):
    try:
        obj = ProjectPost.objects.get(id=post_id)
    except:
        raise Http404
    template_name = "blog_post_detail.html"
    context = {'h1': "Project Post", 'project': obj}
    return render(request, template_name, context)
