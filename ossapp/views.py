from django.shortcuts import render
from . models import Product, Category

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def productPage(request):
    category_id=request.GET.get('category')
    data = {}
    if category_id:
        products= Product.get_products_by_categoryid(category_id)
    else:
        products = Product.get_all_products()
    category = Category.get_all_category()
    data['products'] = products
    data['category'] = category
    return render(request, 'product.html', data)


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')