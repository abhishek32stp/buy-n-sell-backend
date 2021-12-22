from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy
from django.core.validators import RegexValidator


from .managers import *


class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(ugettext_lazy('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','phone_no']

    objects = CustomUserManager()

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a Valid Phone number Up to 15 digits.")
    phone_no=models.CharField(validators=[phone_regex], max_length=17, blank=True)
    image=models.ImageField(upload_to='userimages/',default=None,null=True)
    

    def __str__(self):
        return self.email
