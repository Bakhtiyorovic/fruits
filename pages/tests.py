from django.test import TestCase, SimpleTestCase
from .models import *
from .views import *
from .urls import *
from django.urls import reverse, resolve
# Create your tests here.


#tests for models
class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = ContactMessage.objects.create(name= 'Test Name', phone= 'Test Phone', email= 'Test Email', message= 'Test Message')

    def test_contact_name(self):
        self.assertEqual(self.contact.name, 'Test Name')

    def test_contact_phone(self):
        self.assertEqual(self.contact.phone, 'Test Phone')

    def test_contact_email(self):
        self.assertEqual(self.contact.email, 'Test Email')

    def test_contact_message(self):
        self.assertEqual(self.contact.message, 'Test Message')


#tests for views

class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')

#tests for urls





class UrlsTest(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, Home)
