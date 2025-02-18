from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_make_item(self):
        new = Menu.objects.create(name='test', price=10.00, inventory=10)
        self.assertEqual(new.name, 'test')