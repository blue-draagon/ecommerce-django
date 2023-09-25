from category.models import Category


def categories_menu_items(request):
  return {'categories_menu_items': Category.objects.all()}
