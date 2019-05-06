from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pref,City
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

@login_required
def index(request):
  return render(request, 'weather/index.html')

@login_required
def next(request):
  return render(request, 'weather/update.html')

@login_required
def update(request):
  # テーブルを初期化
  prefs = Pref.objects.all()
  prefs.delete();
  citys = City.objects.all()
  citys.delete()
  
  # livedoor提供のcityIDが定義されたxmlファイルを抽出
  url = 'http://weather.livedoor.com/forecast/rss/primary_area.xml'
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as response:
    xml_string = response.read()
  root = ET.fromstring(xml_string)

  # タグを抽出し、テーブルに登録する
  for pref in root.iter('pref'):
    pref_entity = Pref(name=pref.attrib['title'])
    pref_entity.save()
    for city in pref.iter('city'):
      print(city.attrib['id'])
      ciyte_entity = City(pref_id=pref_entity.id ,name=city.attrib['title'], city_id=city.attrib['id'])
      ciyte_entity.save()
  return render(request, 'weather/update.html')