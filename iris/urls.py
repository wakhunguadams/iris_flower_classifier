from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',home_page,name='home'),
]
urlpatterns += staticfiles_urlpatterns()
