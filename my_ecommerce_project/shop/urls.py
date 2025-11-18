

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    # path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list_products'),  # adaugă asta
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),

    # Coș de cumpărături
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),

    # Lista comenzilor
    path('orders/', views.order_list, name='order_list'),

    # Golire cos
    path('cart/clear/', views.clear_cart, name='clear_cart'),

    # Stripe
    path('create-checkout-session/<int:order_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),

]








