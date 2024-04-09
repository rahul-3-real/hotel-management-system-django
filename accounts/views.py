from django.shortcuts import render


# Register View
def register_view(request):
    template_name = "./accounts/register.html"
    context = {}
    return render(request, template_name, context)
