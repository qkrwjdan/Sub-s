from django.shortcuts import render,redirect
from .models import UsingPlan,Service
from .forms import SearchForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.utils.simplejson import dumps, loads, JSONEncoder
from json import dumps,loads


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        svc = []
        # 사용자가 사용하고 있는 요금제 정보 : plan
        plan = UsingPlan.objects.filter(user = request.user)
        for i in plan:
            data = Service.objects.get(
                service_name = i.service.service_name,
                plan_name = i.service.plan_name
            )
            svc.append(data)
        
        data_list = svc
        return render(request,'index.html',{
            "data" : data_list,
        })
    return render(request,'index.html')

def mysubs(request):
    if not request.user.is_authenticated :
        return render(request,'mysubs_notLogin.html')

    if request.method == 'POST':
        # if 'searchwords' in request.POST:
        #     # findthis = 찾고자 하는 문자열
        #     findthis = request.POST['searchwords']
        findthis = request.POST['searchwords']
        contents = []
        # getSearchResults() 메소드 구현 필요
        contents = getSearchResults(findthis)
        #dumps = 딕셔너리 객체를 json문자열로 변환한다.
        #contents 는 dictionary 타입인가?
        json = dumps(contents)
        return HttpResponse(json)
    else:
        #refactoring이 필요하다 object를 가져오는 더 나은 방법이 있을거다.
        us = User.objects.get(username = request.user)
        plan = UsingPlan.objects.filter(user = us)
        return render(request,'mysubs.html',{
            'us' : us, 'plan' : plan,
        })

def mysubsAdd(request):
    if request.method == 'POST':
        # if 'searchwords' in request.POST:
        #     # findthis = 찾고자 하는 문자열
        #     findthis = request.POST['searchwords']
        findthis = request.POST['searchwords']
        contents = []
        # getSearchResults() 메소드 구현 필요
        contents = getSearchResults(findthis)
        #dumps = 딕셔너리 객체를 json문자열로 변환한다.
        #contents 는 dictionary 타입인가?
        json = dumps(contents)
        return HttpResponse(json)
    else:
        return render(request,'mysubs_add.html')


def getSearchResults(findthis):
    """
    findthis(str)을 받아서
    DB 에서 
    data(list)를 반환해줌
    """
    # obj 는 DB에서 찾은 query들의 리스트 객체
    obj = Service.objects.filter(service_name__contains = findthis)
    data = []
    for i in obj:
        response_data = i.service_name #str 
        data.append({'result' : response_data})
    return data   

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

