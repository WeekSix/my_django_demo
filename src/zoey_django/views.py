# Model View Template(MVT)
from django.http import HttpResponse
from django.shortcuts import render

# one web view is one function in this views.py file
def home_page(request):
#     return HttpResponse("<h1>My Home Page</h1>")
    return render(request, "home_page.html")

def about_page(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")