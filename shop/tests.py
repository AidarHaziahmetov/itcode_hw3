
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
        response = self.client.post(url, {'name': "new_name"},format="json")
        # self.assertNotEqual(response, "new_name")
        print(old_name)
        self.product.refresh_from_db()
        print(models.Product.objects.get(pk=self.product.pk).name)
        self.assertEqual(response.status_code, 302)

    def test_delete_product(self):
        url = reverse('product_delete', kwargs={'pk': self.product.pk})
        old_product_count = models.Product.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_product_count, models.Product.objects.count())

    # def test_create_product(self):
    #     url = reverse('product_create')
    #     # new_product = factories.ProductFactory()
    #     old_product_count = models.Product.objects.count()
    #     print(models.Product.objects.all())
    #     response = self.client.post(url, {
    #         'name': 'new_name1',
    #         'price': self.product.price+1,
    #         'description': self.product.description,
    #         'image': self.product.image,
    #         'category': self.product.category,
    #         'stock': self.product.stock,
    #         'created': self.product.created,
    #         'updated': self.product.updated,
    #     })
    #     self.product.refresh_from_db()
    #     print(models.Product.objects.all())
    #     self.assertEqual(response.status_code, 302)
    #     self.assertLess(old_product_count, models.Product.objects.count())
