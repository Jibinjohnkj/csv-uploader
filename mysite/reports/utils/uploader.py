import csv
from datetime import datetime

from reports.models import Product


def process_products(document, headers):
    reader = csv.DictReader(document, fieldnames = headers, quoting=csv.QUOTE_NONE)
    for row in reader:
        try:
            p = Product(inventory_key=int(row['inventory_key']),
                        catalog_no=row['catalog_no'],
                        catalog_color=row['catalog_color'],
                        size=row['size'],
                        quantity=int(row['quantity']),
                        catalog_price = float(row['case_price']))

            if row['sale_end_datetime']:
                # if sale_end_datetime is greater than today, then catalog_price is mapped from case_sale_price
                # in the csv file, and is_on_sale should be set to True
                if datetime.strptime(row['sale_end_datetime'], '%m/%d/%y %H:%M:%S') > datetime.now():
                   p.catalog_price = float(row['case_sale_price'])
                   p.is_on_sale = True
            p.save()
        except ValueError:
            pass




