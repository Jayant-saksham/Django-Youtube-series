from django.shortcuts import render
from store.models.product import Product, Category

# Create your views here.
def home(request):
	allProducts = Product.objects.all()
	allCategories = Category.objects.all()
	category_id = request.GET.get('category', None)
	if category_id is not None:
		allProducts = Product.getProductByID(category_id)
	data = {
		'products' : allProducts,
		'categories' : allCategories
	}
	return render(request, 'index.html', data)