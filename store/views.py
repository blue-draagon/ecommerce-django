from django.shortcuts import render

from store.context_processor import store_context, product_detail_context


def store(request, category_slug=None):
  return render(request, 'store/store.html', store_context(category_slug))


def product_detail(request, product_slug, category_slug=None):
  return render(request, 'store/product_detail.html', product_detail_context(product_slug))
