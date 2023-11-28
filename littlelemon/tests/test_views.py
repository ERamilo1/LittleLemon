from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=8, inventory=100)
        Menu.objects.create(title="Pasta", price=20, inventory=80)
        Menu.objects.create(title="Chicken", price=25, inventory=70)

    def test_getall(self):
        client = APIClient()
        user = User.objects.create_user(username='admin', password='lemon278!')
        client.force_authenticate(user=user)
        response = client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        menu_items_serialized = MenuSerializer(menu_items, many=True)
        self.assertEqual(menu_items_serialized.data, response.data)
        client.logout()