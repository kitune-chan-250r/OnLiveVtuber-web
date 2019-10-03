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


    #testdata
    livedata.append({'liver_name': "testdata",
                     'live_url': "PWfXvA3E2fo",
                     'live_title': "【クレヨンしんちゃん】ぽんこつ園児の団長がっょっょ目指して冒険だ～！【ホロライブ/白銀ノエル】", #10文字
                     'start_time': "00:00:00",
                     'gender': "male",
                     'production': "hololive"})
    livedata.append({'liver_name': "testdata",
                     'live_url': "PWfXvA3E2fo",
                     'live_title': "【クレヨンしんちゃん】ぽんこつ園児の団長がっょっょ目指して冒険だ～！【ホロライブ/白銀ノエル】", #10文字
                     'start_time': "00:00:00",
                     'gender': "male",
                     'production': "hololive"})
    
    data['livedata'] = livedata

    print(data)
    return render(request, 'index.html', data)

