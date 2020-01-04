from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def mysubs(request):
    return render(request,'mysubs.html')

def recommend(request):
    return render(request,'recommend.html')

def honey(request):
    return render(request,'honey.html')

def magazine(request):
    return render(request,'magazine.html')

def event(request):
    return render(request,'event.html')

def notice(request):
    return render(request,'notice.html')

def profile(request):
    return render(request,'profile.html')

