
from django.test import TestCase
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        self.client = APIClient()  # Initialize the API client
        Menu.objects.create(name="Pizza", price=10.99, inventory=10)
        Menu.objects.create(name="Pasta", price=8.99, inventory=5)
        Menu.objects.create(name="Salad", price=5.99, inventory=3)
