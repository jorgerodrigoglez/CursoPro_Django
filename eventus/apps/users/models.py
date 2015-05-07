from django.db import models
#para crear el modelo de usuarios hay que importar auth.models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager, models.Manager):

	def create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		email = self.normalize_email(email)

		if not email:
			raise ValueError('El EMAIL es obligatorio')
		
		user = self.model(username = username, email = email, is_active = True, is_staff = is_staff, is_superuser = is_superuser, **extra_fields)

		user.set_password(password)
		user.save(using = self_db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length = 100, unique = True)#hay que ponerlo antes de realizar las migraciones, ya que este usuario debe ser unico
	email = models.EmailField()
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	avatar = models.URLField(upload_to = 'user') #falta la carpeta user

	object = UserManager()

	is_active = django.db.models.BooleanField(default=True)
	is_staff = django.db.models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELD = ['email']

	def get_short_name(self):
		return self.username