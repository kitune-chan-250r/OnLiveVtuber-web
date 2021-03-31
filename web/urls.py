from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('reminder', reminder, name='reminder'),
    path('vtuber', vtuber, name='vtuber'),
    path('about_this_page', about_this_page, name='about_this_page'),
]