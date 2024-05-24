from django.db import models
from enum import IntEnum

class Ranking(IntEnum):
  MINIMUM = 1
  MEH = 2
  AVERAGE = 3
  AMAZING = 4
  PERFECT = 5
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class JobListing(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField()
    date_posted = models.DateTimeField
    ranking = models.IntegerField(choices=Ranking.choices(), default=Ranking.AVERAGE)

