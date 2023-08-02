from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Restaurant
from .models import Menu, MenuItem
import datetime
import decimal

class MenuSerializerTest(APITestCase):
    def test_create_menu(self):
        restaurant = Restaurant.objects.create(name="Test Restaurant")
        payload = {
            "name": "Test Menu",
            "restaurant_name": "Test Restaurant",
            "date": "2023-08-20",
            "items": [
                {
                    "name": "Item 1",
                    "description": "Item 1 Description",
                    "price": "9.99"
                },
                {
                    "name": "Item 2",
                    "description": "Item 2 Description",
                    "price": "19.99"
                }
            ]
        }
        url = reverse('menu-list')  # Assuming the URL pattern for creating menus is named 'menu-list'
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the menu and menu items are created correctly in the database
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(MenuItem.objects.count(), 2)

        menu = Menu.objects.first()
        self.assertEqual(menu.name, "Test Menu")
        self.assertEqual(menu.restaurant.name, "Test Restaurant")
        self.assertEqual(menu.date, datetime.date(2023, 8, 20))

        item1 = MenuItem.objects.get(name="Item 1")
        self.assertEqual(item1.description, "Item 1 Description")
        self.assertEqual(item1.price, decimal.Decimal("9.99"))

        item2 = MenuItem.objects.get(name="Item 2")
        self.assertEqual(item2.description, "Item 2 Description")
        self.assertEqual(item2.price, decimal.Decimal("19.99"))

        # Check if the menu items are associated with the menu
        self.assertEqual(menu.items.count(), 2)
        self.assertIn(item1, menu.items.all())
        self.assertIn(item2, menu.items.all())