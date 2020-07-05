from django.db import models


class Shop(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='shop/images')

	def __str__(self):
		return self.title