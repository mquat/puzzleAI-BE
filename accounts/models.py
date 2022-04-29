from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, last_name, first_name, password = None):
        user = self.model(
            email       = self.normalize_email(email),
            last_name   = last_name,
            first_name  = first_name,
        )
        user.set_password(password)
        user.is_superuser = False 
        user.is_active    = True

        user.save(using = self._db)
        return user 

    def create_superuser(self, email, last_name, first_name, password = None):
        user = self.create_user(
            email       = self.normalize_email(email),
            last_name   = last_name, 
            first_name  = first_name, 
            password    = password,
        )
        user.is_superuser = True
        user.is_active    = True

        user.save(using = self._db)
        return user 

class User(AbstractBaseUser):  
    email = models.EmailField(
        max_length = 100,
        null       = False, 
        unique     = True
    )
    last_name = models.CharField(
        max_length = 50,
        null       = False,
    )
    first_name = models.CharField(
        max_length = 50,
        null       = True, 
    )
    date_joined  = models.DateTimeField(auto_now_add = True)
    is_superuser = models.BooleanField(default = False)
    is_active    = models.BooleanField(default = True)

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'password']
    
    def __str__(self): 
        return self.email 
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser