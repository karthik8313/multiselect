from django.db import models
from multiselectfield import MultiSelectField

class multi(models.Model):
	name=models.CharField(max_length=50)
	lang=models.CharField(
		max_length=30,
		choices=(
			('En','English'),
			('Tm','Tamil'),
			('Kn','Kannada'),
			('Tl','Telugu'),
			)
		)
	title=MultiSelectField(max_length=50,choices=(('a','apple'),('m','mango'),('o','orrange'),
		),max_choices=2)
	def __str__(self):
		return self.name
	