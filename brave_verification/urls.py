from django.urls import path
from .views import verification_txt

urlpatterns = [
    path("brave-rewards-verification.txt", verification_txt),
]
