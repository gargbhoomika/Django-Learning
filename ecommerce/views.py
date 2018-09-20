from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contact_Form

def home_page(request):
    content = {
    "title" : "Home Page Working" ,
    "words" : "This is a Home Page."
    }
    return render(request, "home_page.html" , content)

def about_page(request):
    content = {
    "title" : "About Page  Working" ,
    "words" : "This is a About Page."
    }
    return render(request, "home_page.html" , content)

def contact_page(request):
    contact_form = Contact_Form(request.POST or None)

    content = {
    "title" : "Contact Page Working" ,
    "words" : "This is a Contact Page." ,
    "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('full_name'))
    #     print(request.POST.get('emailid'))
    #     print(request.POST.get('content'))

    return render(request, "contact/view.html" , content)
