from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from orders.models import Order
from .forms import OrderForm
from pupestore.context_processors import global_context 


def checkout(request):

    context = global_context(request)['global_context']
    print()
    print()
    print('QUANTITY CONTEXT IN CHECKOUT')
    print(context['get_quantity'])
    print()
    print()
    
    # if context['get_quantity'] == 0 or context['get_value'] == 0 or list(context.cart_session.keys())<1:
    messages.warning(request, 'Your cart is empty, please add a product to it to be able to checkout!')
    return redirect(reverse('products'))

    # else:
    #     pass

    # order_form = OrderForm()
    # context = {
    #     'order_form' : order_form,
    # }

    return render(request, 'checkout/checkout.html', context)