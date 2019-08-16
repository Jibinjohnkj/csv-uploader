from django.test import TestCase
from reports.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(inventory_key=864,
                               catalog_no="29M",
                               catalog_color="White",
                               size="S",
                               quantity="500",
                               catalog_price="2.17")

        Product.objects.create(inventory_key="864",
                               catalog_no="29M",
                               catalog_color="White",
                               size="M",
                               quantity="415",
                               catalog_price="5.27",
                               is_on_sale=True)

    def test_products_saving_works(self):
        """Product saving works as expected"""
        self.assertEqual(Product.objects.count(), 2)
