from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm


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
    template_name = "./accounts/login.html"
    context = {}
    return render(request, template_name, context)


# Logout View
def logout_view(request):
    template_name = "./accounts/logout.html"
    context = {}
    return render(request, template_name, context)
