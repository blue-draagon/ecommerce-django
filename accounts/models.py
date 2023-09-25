from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
  def create_user(self, firstname, lastname, username, email, password=None):
    if not email:
      raise ValueError('Un utilisateur doit avoir une adresse email')
    if not username:
      raise ValueError('Un utilisateur doit avoir un nom d\'utilisateur ')

    user = self.model(
      email=self.normalize_email(email),
      username=username,
      firstname=firstname,
      lastname=lastname,
    )

    user.set_password(password)

    user.save(using=self._db)

    return user

  def create_superuser(self, firstname, lastname, username, email, password=None):
    user = self.create_user(firstname, lastname, username, email, password)
    user.is_admin = True
    user.is_staff = True
    user.is_active = True
    user.is_superadmin = True

    user.save(using=self._db)

    return user


class Account(AbstractBaseUser):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=20)

  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  phone = models.CharField(max_length=20, unique=True)

  # required field
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now_add=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  is_superadmin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

  objects = MyAccountManager()

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, add_label):
    return True
