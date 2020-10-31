from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from products.models import Product
from orders.models import Order, OrderProduct
from .forms import OrderForm
from pupestore.context_processors import global_context 
from storemain.utils import is_valid_uuid
import uuid
import json
import stripe

def checkout(request):

    context = global_context(request)['global_context']
    cart_session = context['cart_session']
    order_id_session = context['order_id']
    stripe_total = round(context['get_value']  * 100)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)
    
    if context['get_quantity'] == 0 or \
        context['get_value']  == 0:
        # or len(list(cart_session.keys())) < 1:
        messages.warning(request, 
        'Your cart is empty, please add products to be able to checkout!')
        return redirect(reverse('products'))

    else:

        if request.user.is_authenticated:
            # here no get or create
            # as by then order should have
            # been already created
            order = get_object_or_404(Order, user=request.user, 
            in_cart=True)

        else:
    
            if order_id_session != None:
                order = get_object_or_404(Order, id=order_id_session , 
                in_cart=True)

            else: 
                order = Order(in_cart=True)
                order.save()
                context['order_id'] = str(order)
         

            for cart_session_item_id in list(context['cart_session'].keys()):
                if is_valid_uuid(cart_session_item_id):
                    product = get_object_or_404(Product, 
                    pk=cart_session_item_id)
                    orderproduct = OrderProduct(order=order, 
                    product=product)
                    orderproduct.quantity = cart_session[cart_session_item_id]
                    orderproduct.save()

            # for a guest order 'in cart' to persist during the session
            request.session['order_id'] = context['order_id'] 

            context = {
                'order_form' : order_form,
                'order' : order,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
                'client_secret': intent.client_secret,
               
            }

        return render(request, 'checkout/checkout.html', context)

def checkout_process(request):

        if request.method == "POST": 
            data = json.loads(request.body)
            email = data['email']

            context = global_context(request)['global_context']
            order_id_session = context['order_id']
            order = get_object_or_404(Order, id=order_id_session , 
                    in_cart=True)
            order.in_cart = False
            order.paid = True
            order.email = email
            order.save()

            # emptying cart and other session info
           
            del request.session['cart_session']
            
            return JsonResponse('Order processed', safe=False)

def checkout_success(request):

        messages.success(request, 'Order successfully completed!')
        return redirect('index')


def checkout_failure(request):

        messages.warning(request, 'Checkout failed please try again!')
        return redirect('checkout')
