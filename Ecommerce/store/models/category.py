from django.db import models

class Category(models.Model):
	category_name = models.CharField(max_length=50, default="Default")

	def __str__(self):
		return self.category_name


