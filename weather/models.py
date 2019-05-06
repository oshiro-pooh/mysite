from django.db import models

class Pref(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class City(models.Model):
  pref = models.ForeignKey(Pref, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  city_id = models.CharField(max_length=6)

  def __str__(self):
    return self.name