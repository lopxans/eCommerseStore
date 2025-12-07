from django.shortcuts import render
from .models import Product, Category

def home(request):
    product = Product.objects.all()
    
    return render(request, 'core/index.html', {'product': product})
