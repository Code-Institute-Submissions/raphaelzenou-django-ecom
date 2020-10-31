from django.shortcuts import render
from products.models import Product

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # https://docs.djangoproject.com/en/3.1/intro/tutorial03/
    context = {
        'page': 'Home',
        'products': Product.objects.all(),
    }
    return render(request, 'storemain/index.html', context)

