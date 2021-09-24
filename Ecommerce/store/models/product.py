from django.db import models
from store.models.category import Category

class Product(models.Model):
	name = models.CharField(max_length=50, default="")
	price = models.PositiveIntegerField(default=0)
	desc = models.CharField(max_length=200, default="")
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	image = models.ImageField(upload_to="uploads/products")

	@staticmethod
	def getProductByID(id):
		if id:
			return Product.objects.filter(category  = id)
		else:
			return Product.objects.all()


	def __str__(self):
		return self.name