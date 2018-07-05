# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
import csv
import django
import datetime
import sys, os

csv_filepathname="/Users/yogeshnaren/Learning/UC Masters in Data Science/Spring 2018/Cloud Computing/Project/Assignment II - RESTful API/Weather_Forecast/webapp/daily.csv"

# Create your models here.
class weather(models.Model) :
	DATE = models.CharField(max_length=10, primary_key = True)
	TMAX = models.FloatField()
	TMIN = models.FloatField()

	def __str__(self) :
		return self.date