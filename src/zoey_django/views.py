# Model View Template(MVT)
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# one web view is one function in this views.py file
def home_page(request):
    my_title = "My Home Page"
    context = {"h1":my_title, "title":"HOME", "button_text":"Home Button", "my_list":[1,2,3,4,5]}
    return render(request, "home_page.html", context)

def about_page(request):
    return render(request, "about_page.html", {"h1":"About us", "title":"ABOUT"})

def contact_page(request):
    return render(request, "contact_page.html", {"h1":"Contact us", "title":"CONTACT"})

def example(request):
    context = {"h1":"Example", "title":"HOME"}
    template_name = "Strings.txt"
    # template_name = "Strings-ch.txt"
    template_obj    = get_template(template_name)
    rendered_string  = template_obj.render(context)
    return render(request, "about_page.html", {"text_file": rendered_string, "h1":"Example"})