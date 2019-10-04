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

    #test
    livedata.append({'liver_name': 'test name pr=にじさんじ',
                     'live_url': 'Sun-ggImuVg',
                     'live_title': 'test title',
                     'start_time': '00:00:00',
                     'gender': 'woman',
                     'production': 'にじさんじ'})

    livedata.append({'liver_name': 'test name pr=ホロライブ',
                     'live_url': 'Sun-ggImuVg',
                     'live_title': 'test title',
                     'start_time': '00:00:00',
                     'gender': 'man',
                     'production': 'ホロライブ'})



    #data

    data['livedata'] = livedata
    print(data)
    return render(request, 'index.html', data)

