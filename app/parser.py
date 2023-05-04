# from django.core.management.base import BaseCommand
import os
import django
from app.models import Products
from bs4 import BeautifulSoup
import requests


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monyedi.settings')
# django.setup()

# class Command(BaseCommand):
# def handle(self, *args, **options):

    # products = Products.objects.all()
    # for product in products:
    #     url = product.url
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #
    #     product.price = soup.find('span', {'class': 'num'}).text.strip()
    #     product.save()

    # self.stdout.write(self.style.SUCCESS('Data has been successfully parsed and saved to the database.'))
