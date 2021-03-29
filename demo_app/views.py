from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context{
        "allModels" : ExampleModel.objects.all()
    }
    return render("hello!")

def create(request):
    ExampleModel.objects.create(
        name = request.POST["name"]
    )
    return redirect("/")