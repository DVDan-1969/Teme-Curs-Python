
from shop.models import Product, Order, OrderItem, Category
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import ShippingAddress



class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
    def test_register_and_login(self):
        # Creăm user nou
        user = User.objects.create_user(username='newuser', password='12345')
        login = self.client.login(username='newuser', password='12345')
        self.assertTrue(login)

    def test_login_required_cart(self):
        response = self.client.get('/shop/cart/')
        self.assertEqual(response.status_code, 302)  # redirecționează la login


class CartTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            price=100,
            available=True
        )
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_add_to_cart(self):
        response = self.client.post(f'/shop/cart/add/{self.product.id}/', {'quantity': 2})
        order = Order.objects.filter(customer=self.user, completed=False).first()
        self.assertIsNotNone(order)
        self.assertEqual(order.items.count(), 1)
        self.assertEqual(order.items.first().quantity, 2)

    def test_clear_cart(self):
        order = Order.objects.create(customer=self.user, completed=False)
        OrderItem.objects.create(order=order, product=self.product, quantity=1)
        response = self.client.get('/shop/cart/clear/')
        self.assertEqual(response.status_code, 302)  # redirect după golire
        order = Order.objects.filter(customer=self.user, completed=False).first()
        self.assertIsNone(order)

    def test_cart_total(self):
        order = Order.objects.create(customer=self.user, completed=False)
        OrderItem.objects.create(order=order, product=self.product, quantity=3)
        self.assertEqual(order.get_total(), 300)


class CheckoutTests(TestCase):
    def setUp(self):
        # Creăm categoria și produsul de test
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            price=100,
            available=True
        )

        # Creăm utilizatorul și clientul de test
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_checkout_empty_cart(self):
        # Cerere GET la checkout cu coș gol
        response = self.client.get('/shop/checkout/')
        self.assertContains(response, "empty", status_code=200)

    def test_checkout_with_products(self):
        # Creăm un order și adăugăm un produs
        order = Order.objects.create(customer=self.user, completed=False)
        OrderItem.objects.create(order=order, product=self.product, quantity=2)

        # Cerere GET la checkout pentru a vedea formularul
        response = self.client.get('/shop/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('order', response.context)

    def test_submit_checkout_form(self):
        # Creăm un order și adăugăm un produs
        order = Order.objects.create(customer=self.user, completed=False)
        OrderItem.objects.create(order=order, product=self.product, quantity=2)

        # Trimitem datele formularului
        form_data = {
            'full_name': 'Test User',
            'address': '123 Test Street',
            'city': 'Test City',
            'phone': '0123456789'
        }
        response = self.client.post('/shop/checkout/', data=form_data)

        # Verificăm că order-ul s-a finalizat
        order.refresh_from_db()
        self.assertTrue(order.completed)

        # Verificăm că adresa de livrare a fost creată
        shipping = ShippingAddress.objects.get(order=order)
        self.assertEqual(shipping.full_name, 'Test User')
        self.assertEqual(shipping.city, 'Test City')

        # Verificăm că pagina de succes a fost afișată
        self.assertTemplateUsed(response, 'shop/checkout_success.html')