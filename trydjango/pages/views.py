from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    return render(request=request, template_name="home.html", context={})

def contact_view(request, *args, **kwargs):
    return render(request=request, template_name="contact.html", context={})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us!",
        "my_number": 123,
        "my_list": [1,2,3,4,5]
    }
    return render(request=request, template_name="about.html", context=my_context)

def social_view(request, *args, **kwargs):
    return render(request=request, template_name="social.html", context={})