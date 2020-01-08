from django.shortcuts import render,redirect
from .models import UsingPlan,Service
from .forms import SearchForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'index.html')

def mysubs(request):
    if not request.user.is_authenticated :
        return render(request,'mysubs_notLogin.html')
    #refactoring이 필요하다 object를 가져오는 더 나은 방법이 있을거다.
    us = User.objects.get(username = request.user)
    plan = UsingPlan.objects.filter(user = us)

    return render(request,'mysubs.html',{
        'us' : us, 'plan' : plan,
    })

def mysubsAdd(request):
    if request.method == 'POST':
        searchF = SearchForm(request.POST)
        print(request.POST['word'])
        if searchF.is_valid():
            word = request.POST['word']
            obj = Service.objects.filter(service_name__contains = word)
            return render(request,'mysubs_add.html',{
                'obj' : obj , 'form' : searchF
            })
        else:
            return render(request,'event.html')
    else:
        searchF = SearchForm()
        return render(request,'mysubs_add.html',{
            'form' : searchF,
        })
        
    

    return render(request,'mysubs_add.html')

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

