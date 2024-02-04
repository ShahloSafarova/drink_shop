from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from .forms import UpdateDrinkForm
from fruits.models import Ichimliklar


class UpdateDrinkViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@example.com',
            password='1234567'
        )
        self.client.login(username='admin', password='1234567')
        self.fruit = FruitsModel.objects.create(
            name='Test Drink',
            price=3.0,
            short_description='quality drinks',
        )
        self.update_drink_url = reverse('update_drink', args=[self.drink.id])

    def test_update_drink_view_get(self):
        response = self.client.get(self.update_drink_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ichimlik/update_ichimlik.html')
        self.assertIsInstance(response.context['form'], UpdateDrinkForm)
        self.assertEqual(response.context['fruit'], self.fruit)

    def test_update_drink_view_post_valid_data(self):
        updated_name = 'Updated Drink'
        updated_price = 4.0
        updated_short_description = 'Tasty drinks were updates'

        data = {
            'name': updated_name,
            'price': updated_price,
            'short_description': updated_short_description,
        }

        response = self.client.post(self.update_drink_url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ichimlik/aboutichimlik.html')

        updated_drink = Ichimliklar.objects.get(id=self.drink.id)
        self.assertEqual(updated_drink.name, updated_name)
        self.assertEqual(updated_drink.price, updated_price)
        self.assertEqual(updated_drink.short_description, updated_short_description)

class DeleteDrinkViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@example.com',
            password='1234567'
        )
        self.client.login(username='admin', password='1234567')
        self.drink = Ichimliklar.objects.create(
            name='Test Drink',
            price=8.0,
            short_description='Tasty drinks are available'
        )
        self.delete_drink_url = reverse('delete', args=[self.drink.id])

    def test_delete_drink_view_get(self):
        response = self.client.get(self.delete_fruit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ichimlik/delete.html')
        self.assertEqual(response.context['drink'], self.drink)

    def test_delete_drink_view_post(self):
        response = self.client.post(self.delete_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ichimlik/ichimlik.html')

        self.assertFalse(Ichimliklar.objects.filter(id=self.drink.id).exists())
