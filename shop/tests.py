
from django.test import TestCase
from django.urls import reverse

from shop import factories, models


# Create your tests here.
class ShopTestCase(TestCase):
    def setUp(self):
        self.product = factories.ProductFactory()

    def test_get_product_list(self):
        url = reverse('catalog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), models.Product.objects.count())

    def test_get_product_detail(self):
        url = reverse('product_detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        url = reverse('product_update', kwargs={'pk': self.product.pk})
        old_name = self.product.name
        old_price = self.product.price
        old_description = self.product.description
        old_stock = self.product.stock
        response = self.client.post(url, {
            'name': "new_name",
            'price': old_price,
            'description': old_description,
            'stock': old_stock
        })
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.product.name, old_name)

    def test_delete_product(self):
        url = reverse('product_delete', kwargs={'pk': self.product.pk})
        old_product_count = models.Product.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_product_count, models.Product.objects.count())

    def test_create_product(self):
        url = reverse('product_create')
        old_products_count = models.Product.objects.count()
        response = self.client.post(url, {
            'name': 'new_name1',
            'price': self.product.price + 1,
            'description': self.product.description,
            'stock': self.product.stock
        })
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertLess(old_products_count, models.Product.objects.count())
        self.assertEqual(models.Product.objects.get(name='new_name1').stock, self.product.stock)