from django.shortcuts import render
from store.context_processor import store_context


def home(request):
  return render(request, 'home.html', store_context())
