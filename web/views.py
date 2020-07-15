from django.shortcuts import render
import re, time
from web import Vtuber_LiveStatus_API_lib as vlsa
from datetime import timedelta
from datetime import datetime
from dateutil.parser import parse
from pytz import timezone


# Create your views here.
BASE_URL = 'https://vtuber-livestatus-api.herokuapp.com/api/'

#str型 timeを受け取り'%Y-%m-%d %H:%M:%S'のdatetime.timedeltを返す
def time_jst(time):
    p = parse(time).astimezone(timezone('Asia/Tokyo'))
    return parse(p.strftime('%Y-%m-%d %H:%M:%S'))

#str型　startを受け取りdatetime.timedeltのpastを返す
def past_time(start):
    now = datetime.now()
    past = time_jst(str(now)) -  time_jst(start)
    return past

def deformed(start):
    secs = past_time(start).total_seconds()
    hours = int(secs / 3600)
    minutes = int(secs / 60) % 60

    if hours > 0:
        return '約{}時間'.format(hours)
    else:
        return '約{}分'.format(minutes)

def index(request):
    json_data = vlsa.get(BASE_URL + 'onlive/')
    
    data = {}
    livedata = []

    for i in json_data:
        past = deformed(i['start_time'])
        livedata.append({'liver_name': i['uid']['liver_name'],
                         'live_url': i['live_url'].replace('https://www.youtube.com/watch?v=', ''),
                         'live_title': i['live_title'],
                         'past_time': past,
                         'gender': i['uid']['gender'],
                         'production': i['uid']['production']})

    data['livedata'] = livedata
    print(data)
    return render(request, 'index.html', data)

def vtuber(request):
    json_data = vlsa.get(BASE_URL + 'vtuber/')
    data = {}
    data['vtuber'] = json_data
    return render(request, 'vtuber_all.html', data)

def about_this_page(request):
    return render(request, 'about_this_page.html')
