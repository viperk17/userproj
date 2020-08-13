from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# password for test user is Qwerty@1

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered the correct information
        user = authenticate(username=username, password=password)
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
 