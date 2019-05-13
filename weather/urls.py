from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('index', views.index, name='index'),
    path('next', views.next, name='next'),
    path('update', views.update, name='update'),
    path('changePrefs', views.changePrefs, name='changePrefs'),
    path('searchWeather', views.searchWeather, name='searchWeather'),
    path('', views.index, name='index'),
]