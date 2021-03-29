from django.shortcuts import render, redirect, HttpResponse
from .models import ExampleModel

# Create your views here.
def index(request):
    context = {
        'all_the_stuff_from_the_database': ExampleModel.objects.all()
    }
    return render(request, "index.html", context)

def add_new_thing(request):
    # I am a comment
    # I don't really do anything

    ExampleModel.objects.create(
        name = request.POST['name'] # this is important!!!
    )

    return redirect('/')