from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'weather/index.html')

@login_required
def next(request):
    return render(request, 'weather/update.html')
