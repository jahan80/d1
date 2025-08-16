

from django.urls import path
from website1.views import *
urlpatterns = [
    #jahantetst1
    path('',home),
    path('about', about),
    path('contact', contact),
]
