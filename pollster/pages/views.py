from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

#login

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'pages/register.html', context)
       
def loginrPage(request):
    context = {}
    return render(request, 'pages/login.html' , context)