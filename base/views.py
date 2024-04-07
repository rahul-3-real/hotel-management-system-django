from django.shortcuts import render

# Create your views here.


# Index Page
def index(request):
    template_name = "./base/index.html"
    return render(request, template_name)
