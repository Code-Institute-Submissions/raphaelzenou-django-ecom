from django.shortcuts import render, redirect
from .models import Order, OrderProduct
from products.models import Product

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

from django.http import JsonResponse
import json

from pupestore.context_processors import global_context 

def cart(request):

    # global_context = global_context(request) 
    # format : {'global_context': global_context}
    # e.g. global_context.cart_items
    # get_total = global_context['get_total']

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, in_cart=True)
        orderproducts = order.orderproduct_set.all().order_by('product__title')
        context = {
            'page': 'Cart',
            'user': request.user,
            'order': order,
            'orderproducts': orderproducts,
        }
        return render(request, 'orders/cart.html', context)
    else:
        context = {
            'page': 'Cart',
        }
        return render(request, 'orders/cart.html', context)

def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['cartAction']
    url = data['pageUrl']
    page = data['pageName']

    # updating items from the session
    # for logged in users
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(user=request.user, in_cart=True)
        orderproduct, created = OrderProduct.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderproduct.quantity = orderproduct.quantity + 1
            if page.lower() != 'cart':
                messages.success(request, product.title  + ' added to your cart! Click <a href="/orders/cart">here</a> to access it.')
                
        elif action == 'remove':
            orderproduct.quantity = orderproduct.quantity - 1 
        elif action == 'delete':
            orderproduct.quantity = 0 

        orderproduct.save()

        if orderproduct.quantity <=0:
            orderproduct.delete()
            messages.warning(request, product.title  + ' removed from cart!')
    # updating items from the session
    # for all types of users
    cart_session = request.session.get('cart_session', {})
    if productId in list(cart_session.keys()):
        if action == 'add':
            cart_session[productId] += 1
        elif action == 'remove':
            cart_session[productId] -= 1
        elif action == 'delete':
            cart_session[productId] = 0
    else:
        if action == 'add':
            cart_session[productId] = 1
        
    if cart_session[productId] <= 0:
        del cart_session[productId]
        request.session.modified = True
    
    request.session['cart_session'] = cart_session

    return JsonResponse('Order product quantity updated', safe=False)

