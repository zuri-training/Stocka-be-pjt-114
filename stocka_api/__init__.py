# from django.urls import include, path, reverse
# from rest_framework.test import APITestCase, URLPatternsTestCase


# class AccountTests(APITestCase, URLPatternsTestCase):
#     urlpatterns = [
#         path('api/', include('api.urls')),
#     ]

#     def test_create_account(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('account-list')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)