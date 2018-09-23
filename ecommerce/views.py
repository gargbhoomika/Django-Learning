from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Contact_Form, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
def home_page(request):
    content = {
    "title" : "Home Page Working" ,
    "words" : "This is a Home Page."
    }
    if request.user.is_authenticated:
        content["Logged_content"] = "Finally Logged In"
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
    context = {
        "form" : form
    }
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
            return redirect("/")
        else:
            print("Error")
    return render(request, "auth/login.html",context)
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html",context)
