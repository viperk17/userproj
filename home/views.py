from django.shortcuts import render, redirect

# password for test user is Qwerty@1

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
 