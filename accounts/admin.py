from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


# Register your models here.

class AccountAdmin(UserAdmin):
  list_display = ('firstname', 'lastname', 'username', 'email', 'date_joined', 'last_login', 'is_active')
  readonly_fields = ('date_joined', 'last_login')
  ordering = ('-date_joined',)

  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()


admin.site.register(Account, AccountAdmin)
