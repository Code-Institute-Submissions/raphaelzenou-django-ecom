from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from orders.models import Order, OrderProduct
from products.models import Product
import uuid

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def global_context(request):
    # context processor for all pages
    # taking care of guest and 
    # logged in users cart or 'in cart' order 
    # data 
    global_context = {}
    cart_session = request.session.get('cart_session', {})
    cart_items = []
    get_value = 0
    get_quantity = 0
    shipping_required = False
    for item_id, quantity in cart_session.items():
        product = get_object_or_404(Product, pk=item_id)
        get_value += quantity * product.price_in_base_currency
        get_quantity += quantity
        if product.category != 'DIG':
            shipping_required = True

        cart_items.append({
            'id': item_id,
            'get_quantity': get_quantity,
            'get_value': get_value,
            'product': product,
        })

    if get_value < settings.FREE_DELIVERY_THRESHOLD:
        delivery = 10 
        # flat fee
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - get_value
    else:
        delivery = 0
        free_delivery_delta = 0
    
    get_all_in_value = delivery + get_value
        
    global_context = {
        'cart_session': cart_session,
        'cart_items': cart_items,
        'get_value': get_value,
        'get_quantity': get_quantity,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'get_all_in_value': get_all_in_value,
        'current_page':request.path,
        'shipping_required': shipping_required,
    }

    if request.user.is_authenticated:

        order, created = Order.objects.get_or_create(user=request.user, in_cart=True)

        # joining user 'in cart' order and cart in session if any
        if cart_session and len(list(cart_session.keys())) > 0:
            # guest cart session overwrites orderproduct quantities 
            # in the persisting 'in cart' order
            # otherwise user will feel like they are increasing for no reason 
            # if they forgot between two logged in sessions

            for cart_session_item_id in list(cart_session.keys()):
                if is_valid_uuid(cart_session_item_id):
                    product = get_object_or_404(Product, pk=cart_session_item_id)
                    orderproduct, created = OrderProduct.objects.get_or_create(order=order, product=product)
                    orderproduct.quantity = cart_session[cart_session_item_id]
                    orderproduct.save()
                    # del cart_session[cartSessionItem]
                    # request.session.modified = True

        # check if there is anything in 
        # the persisting cart 
        # upon login, just for display
        # cart items are not reintegrated here
        # as 'in cart' order takes priority vs session 
        # when user is logged in
        get_quantity = order.get_quantity
            
        order.delivery_cost = delivery
        order.shipping_required = shipping_required
        order.save()

    global_context = {
    'cart_session': cart_session,
    'cart_items': cart_items,
    'get_value': get_value,
    'get_quantity': get_quantity,
    'delivery': delivery,
    'free_delivery_delta': free_delivery_delta,
    'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    'get_all_in_value': get_all_in_value,
    'current_page':request.path,
    'shipping_required': shipping_required,
    }

    return {'global_context': global_context}