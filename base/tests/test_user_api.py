from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User


class UserListViewTest(APITestCase):
    users_url = reverse("user_list")


    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test')


    def test_user_list_view_with_valid_credentials(self):
        # Authenticate with valid credentials
        self.client.force_authenticate(user=self.user)

        # Make a GET request to the UserListView
        response = self.client.get(self.users_url)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_list_view_with_invalid_credentials(self):
        response = self.client.get(self.users_url)  
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
