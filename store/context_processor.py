from django.shortcuts import get_object_or_404

from category.models import Category
from store.models import Product


def store_context(category_slug=None):
  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)
  else:
    products = Product.objects.filter(is_available=True)

  return {'products': products}


def product_detail_context(product_slug):
  product = get_object_or_404(Product, slug=product_slug)

  return {'product': product}
