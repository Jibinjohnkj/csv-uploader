from django.db import models


class Product(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Xtra Large'),
        ('2XL', 'Double Xtra Large'),
        ('3XL', 'Triple Xtra Large'),
    )

    inventory_key = models.IntegerField()
    catalog_no = models.CharField(max_length=4)
    catalog_color = models.CharField(max_length=24)
    size = models.CharField(choices=SHIRT_SIZES, max_length=4)
    quantity = models.IntegerField()
    catalog_price = models.FloatField()
    is_on_sale = models.BooleanField(default=False)


