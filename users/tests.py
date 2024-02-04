from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.files.uploadedfile import SimpleUploadedFile

class CustomUserSignupTest(TestCase):
    def setUp(self):
        self.signup_url = reverse('sign-up')

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertContains(response, 'form')

    def test_signup_view_post_valid_data(self):
        data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': '1234567',
            'password2': '1234567',
        }
        response = self.client.post(self.signup_url, data, follow=True)

        self.assertTrue(get_user_model().objects.filter(username='admin').exists())
        user = response.context['user']
        self.assertFalse(isinstance(user, AnonymousUser))

        self.assertRedirects(response, reverse('login'))

class CustomUserLoginTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@example.com',
            password='1234567'
        )
        self.login_url = reverse('login')

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'form')

    def test_login_view_post_valid_data(self):
        data = {
            'username': 'admin',
            'password': '1234567',
        }

        response = self.client.post(self.login_url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Hello')
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_view_post_invalid_data(self):
        data = {
            'username': 'admin',
            'password': 'InvalidPassword',
        }

        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'Invalid username or password')

        self.assertFalse(response.context['user'].is_authenticated)

class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@example.com',
            password='1234567'
        )
        self.client.login(username='admin', password='1234567')
        self.profile_url = reverse('profile')

    def test_profile_view_get(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, 'admin')
    def test_profile_view_requires_authentication(self):
        self.client.logout()

        response = self.client.get(self.profile_url)

        self.assertRedirects(response, reverse('login'))