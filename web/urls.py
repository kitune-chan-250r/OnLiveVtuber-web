from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('reminder', reminder, name='reminder'),
    path('vtuber', vtuber, name='vtuber'),
    path('about_this_page', about_this_page, name='about_this_page'),
    path('.well-known', TemplateView.as_view(template_name='brave-rewards-verification.txt', content_type='text/plain'))
]