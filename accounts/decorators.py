from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps


# Auth check Decorator
def is_authenticated(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Please login to access the page.")
            return login_required(view_func)(request, *args, **kwargs)

    return wrapper


# Must not be Authenticated
def must_not_be_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, "You are already authenticated.")
            return redirect("base:index")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper
