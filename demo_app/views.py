from django.shortcuts import render, redirect, HttpResponse
from .models import ExampleModel

# Create your views here.
def index(request):
    context = {
        "all_models" : ExampleModel.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    ExampleModel.objects.create(
        name = request.POST["name"]
    )
    return redirect("/")
