from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Contact_Form, LoginForm
from django.contrib.auth import authenticate, login
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
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, "contact/view.html" , content)

def login_page(request):
    form = LoginForm(request.POST or None)
    print("User Logged In")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request,user)
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")
    context = {
        "form" : form
    }
    return render(request, "auth/login.html",context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html",{})
