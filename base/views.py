from django.shortcuts import render


# Index Page
def index_view(request):
    template_name = "./base/index.html"
    context = {}
    return render(request, template_name, context)
