from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pref,City
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import requests

@login_required
def index(request):
  form = PostForm()
  context = {'form': form, }
  return render(request, 'weather/index.html', context)

@login_required
def someView(request):
    # 同formからのPOSTを各処理へ振り分け
    if 'changePrefs' in request.POST:
      return changePrefs(request)
    elif 'searchWeather' in request.POST:
      return searchWeather(request)

@login_required
def changePrefs(request):
  form = PostForm(request.POST)
  # 都道府県プルダウンの選択値を元に市町村名プルダウンの値を選定するクエリを登録
  form.fields['cities'].queryset = City.objects.filter(pref_id=request.POST['prefs'])
  form.fields['cities'].to_field_name = "city_id"
  context = {'form': form, }
  return render(request, 'weather/index.html', context)
  
@login_required
def searchWeather(request):
  # お天気WebサービスAPIのURL
  url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
  
  form = PostForm(request.POST)
  
  # バリデーションを明示的に呼び出し
  # TODO forms.py の cities の to_field_name起因でエラー発生
  # form.is_valid()
  
  # 都道府県プルダウンの選択値を元に市町村名プルダウンの値を選定するクエリを登録
  form.fields['cities'].queryset = City.objects.filter(pref_id=request.POST['prefs'])
  
  # 市町村名プルダウンの選択値を元に天気を検索する
  city_id = request.POST['cities']
  payload = {'city':city_id}
  tenki_data = requests.get(url, params=payload).json() 

  # 画面出力情報形成
  today_weather = tenki_data['forecasts'][0]['dateLabel'] + ' の天気は ' + tenki_data['forecasts'][0]['telop'] + ' です。'
  tomorrow_weather = tenki_data['forecasts'][1]['dateLabel'] + ' の天気は ' + tenki_data['forecasts'][1]['telop'] + ' です。'
  weather_list = [today_weather, tomorrow_weather]
  context = {'form': form, 'weather_list': weather_list}
  return render(request, 'weather/index.html', context)

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
  
  try:
    # livedoor提供のcityIDが定義されたxmlファイルを抽出
    url = 'http://weather.livedoor.com/forecast/rss/primary_area.xml'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
      xml_string = response.read()
    root = ET.fromstring(xml_string)
  except urllib.error.HTTPError:
    messages.error(request, '元データを取得できませんでした。システム管理者へご連絡下さい。')
    return render(request, 'weather/update.html')

  # タグを抽出し、テーブルに登録する
  for pref in root.iter('pref'):
    pref_entity = Pref(name=pref.attrib['title'])
    pref_entity.save()
    for city in pref.iter('city'):
      ciyte_entity = City(pref_id=pref_entity.id ,name=city.attrib['title'], city_id=city.attrib['id'])
      ciyte_entity.save()
      
  messages.success(request, '更新処理に成功しました。')
  return render(request, 'weather/update.html')