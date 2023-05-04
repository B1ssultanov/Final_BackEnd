# from django.core.management.base import BaseCommand
# from app.models import Products
#
# Products.objects.all().delete()
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         phones = Products.objects.all()
#         for i in phones:
#             products = Products(ID_Products=int(i.id), Categories='Phone')
#             products.save()
