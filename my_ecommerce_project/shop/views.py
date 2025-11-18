

from django.shortcuts import render
from .models import Product, Order, OrderItem
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
import stripe
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404

# Lista de produse disponibile
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})

# Detalii produs
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    form = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})



# Adăugare produs în coș (requiere autentificare)
@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        # Ștergem orice Order incomplet vechi înainte de a crea unul nou
        old_order = Order.objects.filter(customer=request.user, completed=False).first()
        if old_order:
            old_order.items.all().delete()
            old_order.delete()
        # Creăm un Order nou curat
        order = Order.objects.create(customer=request.user, completed=False)
        OrderItem.objects.create(order=order, product=product, quantity=quantity)

    return redirect('shop:cart')


# Vizualizare coș de cumpărături (requiere autentificare)
@login_required
def cart_view(request):
    order = Order.objects.filter(customer=request.user, completed=False).first()
    total = 0
    if order:
        total = sum(item.product.price * item.quantity for item in order.items.all())
    return render(request, 'shop/cart.html', {'order': order, 'total': total})


@login_required
def checkout(request):
    order = Order.objects.filter(customer=request.user, completed=False).first()

    if not order or order.items.count() == 0:
        return render(request, 'shop/checkout.html', {'empty': True})


    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.order = order
            shipping.save()

            order.completed = True
            order.save()

            return render(request, 'shop/checkout_success.html', {'order': order})

    else:
        form = CheckoutForm()

    return render(request, 'shop/checkout.html', {
        'order': order,
        'form': form
    })


# Lista comenzii utilizatorului (requiere autentificare)
@login_required
def order_list(request):
    orders = Order.objects.select_related('customer').prefetch_related('items__product').all()
    return render(request, 'shop/order_list.html', {'orders': orders})

# golire cos
@login_required
def clear_cart(request):
    # Găsim coșul activ al utilizatorului
    order = Order.objects.filter(customer=request.user, completed=False).first()
    if order:
        # Ștergem toate produsele și Order-ul
        order.items.all().delete()
        order.delete()
    return redirect('shop:cart')


@login_required
def create_checkout_session(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user, completed=False)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    YOUR_DOMAIN = "http://127.0.0.1:8000/shop"

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'ron',
                    'product_data': {
                        'name': f"Comanda #{order.id}",
                    },
                    'unit_amount': int(order.get_total() * 100),  # lei → bani
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/payment-success/',
        cancel_url=YOUR_DOMAIN + '/payment-cancel/',
    )

    return redirect(checkout_session.url)

def payment_success(request):
    return render(request, 'shop/payment_success.html')

def payment_cancel(request):
    return render(request, 'shop/payment_cancel.html')


