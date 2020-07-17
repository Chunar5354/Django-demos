from django.db import models

# Create your models here.
class Voltage(models.Model):
	added_date = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Voltage'
