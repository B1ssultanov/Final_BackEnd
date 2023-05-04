from django.db import models
from django.db.models import Model
from unicodedata import category


class Categories(models.Model):
    category = models.CharField('Category of Product', max_length=100)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    category = models.ForeignKey(Categories, models.CASCADE)
    manufacturer = models.CharField('Company', max_length=100)
    name = models.CharField('Name of Product', max_length=100)
    price = models.IntegerField('Price')
    characteristics = models.TextField('Full characteristics of Product')
    image = models.ImageField('Image of Product', upload_to='images/%Y')
    url = models.URLField('URL for this product')

    def __str__(self):
        return f'{Products.name} from {Products.manufacturer} Company.'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
