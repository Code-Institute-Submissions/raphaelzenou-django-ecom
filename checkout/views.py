from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from products.models import Product
from orders.models import Order, OrderProduct
from .forms import OrderForm
from pupestore.context_processors import global_context 
from storemain.utils import is_valid_uuid
import uuid

def checkout(request):

    context = global_context(request)['global_context']
    cart_session = context['cart_session']
    order_id_session = context['order_id']
    print('CONTEXT ORDER ID')
    print('')
    print(order_id_session )
    print('')
    print('CART SESH ')
    print('')
    print(cart_session )
    print('')

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
            print('order ID sessions')
            print(order_id_session)
    
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

            order_form = OrderForm()

            # for a guest order 'in cart' to persist during the session
            request.session['order_id'] = context['order_id'] 

            context = {
                'order_form' : order_form,
                'order' : order,
            }

        return render(request, 'checkout/checkout.html', context)