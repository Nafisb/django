from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.api import views
from base.models import Network
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class NetworkURLTest(SimpleTestCase):

    def test_network_list(self):
        url = reverse('network_list')
        self.assertEquals(resolve(url).func.view_class, views.NetworkListView)


    def test_network_create(self):
        url = reverse('network_create')
        self.assertEquals(resolve(url).func.view_class, views.NetworkCreateView)


class NetworkViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.network = Network.objects.create(title='Test Network')


    def test_network_deletion(self):
        url = reverse('network_delete', kwargs={'id': self.network.pk})
        response = self.client.delete(url) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the network is deleted from the database
        network_exists = Network.objects.filter(pk=self.network.pk).exists()
        self.assertFalse(network_exists, "Network should be deleted from the database")
