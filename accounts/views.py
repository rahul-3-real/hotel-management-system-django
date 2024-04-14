from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm


# Register View
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("accounts:login")
    else:
        form = RegistrationForm()

    template_name = "./accounts/register.html"
    context = {"form": form}
    return render(request, template_name, context)


# Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect("/")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    template_name = "./accounts/login.html"
    context = {"form": form}
    return render(request, template_name, context)


# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("accounts:login")
