from django.shortcuts import render
import re
from web import Vtuber_LiveStatus_API_lib as vlsa
# Create your views here.

def index(request):
    BASE_URL = 'https://vtuber-livestatus-api.herokuapp.com/api/'
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

