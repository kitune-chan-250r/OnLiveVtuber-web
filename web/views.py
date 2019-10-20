from django.shortcuts import render
import re
from web import Vtuber_LiveStatus_API_lib as vlsa
# Create your views here.
BASE_URL = 'https://vtuber-livestatus-api.herokuapp.com/api/'

def index(request):
    json_data = vlsa.get(BASE_URL + 'onlive/')
    
    data = {}
    livedata = []
    for i in json_data:
        livedata.append({'liver_name': i['uid']['liver_name'],
                         'live_url': i['live_url'].replace('https://www.youtube.com/watch?v=', ''),
                         'live_title': i['live_title'],
                         'start_time': i['start_time'],
                         'gender': i['uid']['gender'],
                         'production': i['uid']['production']})

    data['livedata'] = livedata
    print(data)
    return render(request, 'index.html', data)

def vtuber(request):
    json_data = vlsa.get(BASE_URL)
    data = {}
    data['vtuber'] = json_data
    return render(request, 'vtuber_all.html', data)

def about_this_page(request):
    return render(request, 'about_this_page.html')

#pwa
def base_layout(request):
    template='web/base.html'
    return render(request,template)