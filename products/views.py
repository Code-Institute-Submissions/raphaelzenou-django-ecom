from django.shortcuts import render
from products.models import Product

def products(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # https://docs.djangoproject.com/en/3.1/intro/tutorial03/
    context = {
        'page': 'Products',
        'products': Product.objects.filter(active=True),
    }
    return render(request, 'products/products.html', context)

def productDetails(request, pk):
    context = {
        'page': 'Products',
        'product': Product.objects.get(slug=pk),
    }
    return render(request, 'products/product-details.html', context)