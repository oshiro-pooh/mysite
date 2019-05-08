from django.db import models

class Pref(models.Model):
  """
  都道府県テーブル(親)のmodel
  """
  
  # 都道府県名
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class City(models.Model):
  """
  市町村テーブル(子)のmodel
  """
  
  # 都道府県テーブル(親)の主キー
  pref = models.ForeignKey(Pref, on_delete=models.CASCADE)
  # 市町村名
  name = models.CharField(max_length=255)
  # 市町村ID
  city_id = models.CharField(max_length=6)

  def __str__(self):
    return self.name