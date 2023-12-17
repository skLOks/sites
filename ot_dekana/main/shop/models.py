from django.db import models

# Create your models here.
class Tovar(models.Model):
	name = models.CharField(max_length=50)
	infotov = models.CharField(max_length=400)
	price = models.PositiveSmallIntegerField()