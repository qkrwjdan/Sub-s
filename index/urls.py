from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name = 'index'),
    path('mysubs',mysubs,name='mysubs'),
    path('mysubs/add',mysubsAdd,name = 'mysubs_add'),
    path('recommend',recommend,name='service_recommend'),
    path('honey',honey,name='honey_information'),
    path('magazine',magazine,name='magazine'),
    path('event',event,name='event'),
    path('notice',notice,name='notice'),
    path('profile',profile,name='profile'),
]
