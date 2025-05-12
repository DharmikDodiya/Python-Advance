# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from catalog.models import Product

# class ProductAPITestCase(TestCase):
    
#     def setUp(self):
#         self.client = APIClient()
#         self.product = Product.objects.create(
#             name="Test Product",
#             description="Test Description",
#             price=99.99,
#             stock=10
#         )
#         self.valid_payload = {
#             'name': 'New Product',
#             'description': 'New Product Description',
#             'price': '49.99',
#             'stock': 25
#         }
#         self.invalid_payload = {
#             'name': '',
#             'price': '',
#             'stock': ''
#         }

#     def test_list_products(self):
#         response = self.client.get('/api/products/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_product_valid(self):
#         response = self.client.post('/api/products/create', self.valid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['product']['name'], 'New Product')

#     def test_create_product_invalid(self):
#         response = self.client.post('/api/products/create', self.invalid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_retrieve_product(self):
#         response = self.client.get(f'/api/products/{self.product.id}')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['product']['name'], 'Test Product')

#     def test_update_product_valid(self):
#         updated_data = {
#             'name': 'Updated Product',
#             'description': 'Updated Description',
#             'price': '79.99',
#             'stock': 5
#         }
#         response = self.client.put(f'/api/products/update/{self.product.id}', updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['product']['name'], 'Updated Product')

#     def test_update_product_invalid(self):
#         response = self.client.put(f'/api/products/update/{self.product.id}', self.invalid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_delete_product(self):
#         response = self.client.delete(f'/api/products/delete/{self.product.id}')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Product.objects.filter(id=self.product.id).exists())
