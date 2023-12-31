from django.db import models

# Create your models here.
from django.urls import reverse

from category.models import Category


class Product(models.Model):
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  description = models.TextField(max_length=1000, blank=True)
  price = models.IntegerField()
  image = models.ImageField(upload_to='photos/products/', blank=True)
  stock = models.IntegerField()
  is_available = models.BooleanField(default=True)

  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)

  category = models.ForeignKey(Category, on_delete=models.SET(None))

  def __str__(self):
    return self.name

  def sn_price(self):
    return int(self.price * 655)

  def old_price(self):
    return int(self.price * 655 * 1.35)

  def get_url(self):
    return reverse('product_detail', args=[self.category.slug, self.slug])
