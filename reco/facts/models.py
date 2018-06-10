from django.db import models

# Create your models here.

class Case(models.Model):
	title = models.CharField(max_length=250)
	tag = models.CharField(max_length=50)
	name = models.CharField(max_length=250)
	link = models.CharField(max_length=250)

	def __str__(self):
		return self.title