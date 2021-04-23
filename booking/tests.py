from django.test import TestCase,Client
from .models import Storages
from .models import Booking
from login.models import Customer, Admin
import datetime
from django.urls import reverse

"""
class StoragesTestCases(TestCase):
    def setUp(self):
        Admin.objects.create(username=Customer.username)
        manager=Admin.objects.get(username=Customer.username)
        Storages.objects.create(manager=manager,state_name='Gujarat',city_name='Ahmedabad',price=200,is_available=True,storage_location='Bapunagar',start_date='2020-03-20')
        Storages.objects.create(manager=manager,state_name='Rajsthan',city_name='Jaipur',price=150,is_available=True,storage_location='Tilaknagar',start_date='2020-03-26')

    def test_state_name(self):
        room1 = Storages.objects.get(state_name='Gujarat')
        room2 = Storages.objects.get(state_name='Rajsthan')
        self.assertEqual(room1.state_name='Gujarat')
        self.assertEqual(room2.state_name='Rajsthan')
    def test_city_name(self):
        room1 = Storages.objects.get(city_name='Ahmedabad')
        room2 = Storages.objects.get(city_name='Jaipur')
        self.assertEqual(room1.city_name='Ahmedabad')
        self.assertEqual(room2.city_name='Jaipur')
    def test_price(self):
        room1 = Storages.objects.get(price=200)
        room2 = Storages.objects.get(price=150)
        self.assertEqual(room1.price, 200)
        self.assertEqual(room2.price, 150)
class BookingTestCases(TestCase):
    def setUp(self):
        Admin.objects.create(username='yash')
        manager=Admin.objects.get(username='yah')
        Customer.objects.create(username='viral',pin_code=799046)
        Customer.objects.create(username='viral',pin_code=799046)
        Storages.objects.create(city_name='Ahmedabad',storage_location='Bapunagar',start_date='2020-03-09',manager=manager)
        user=Customer.objects.get(username='viral')
        user1=Customer.objects.get(username='yash')
        room=Storages.objects.get(city_name='Ahmedabad')
        Booking.objects.create(user_id=user,city_name=room,amount=100,start_day='2020-03-10',end_day='2020-03-10')
        Booking.objects.create(user_id=user1,city_name=room,amount=200,start_day='2020-03-26',end_day='2020-03-28')

    def test_booking_username(self):
        user=Customer.objects.get(username='yash')
        booking1 = Booking.objects.get(user_id=user)
        user1=Customer.objects.get(username='viral')
        booking2 = Booking.objects.get(user_id=user1)
        self.assertEqual(booking1.user_id.username, 'yash')
        self.assertEqual(booking2.user_id.username, 'viral')
    def test_booking_amount(self):
        booking1 = Booking.objects.get(amount=200)
        booking2 = Booking.objects.get(amount=150)
        self.assertEqual(booking1.amount, 200)
        self.assertEqual(booking2.amount, 150)
    def test_booking_Admin(self):
        booking = Booking.objects.get(amount=150)
        self.assertEqual(booking.city_name.manager.username, 'viral')
class IndexPageViewTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.index_url=reverse('index')
    def test_index_view(self):
        response=self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'booking/index.html')
        """