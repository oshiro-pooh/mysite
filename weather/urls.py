from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('index', views.index, name='index'),
    path('next', views.next, name='next'),
    path('update', views.update, name='update'),
    path('', views.index, name='index'),
]