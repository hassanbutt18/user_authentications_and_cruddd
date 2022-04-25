from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    PLAYER_CHOICES = (
        ("Cricketer", "Cricketer"),
        ("Hockey_Player", "Hockey_Player"),
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)
    gender = models.CharField(max_length=150, null=True)
    player = models.CharField(
        max_length=20,
        choices=PLAYER_CHOICES,
        default="Cricketer",
    )
    npi_number = models.CharField(_('NPI Number'), max_length=225, blank=True)
    job_title = models.CharField(_('Job Title'), max_length=225, blank=True)
    user_Img = models.ImageField(upload_to='images/', default='default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    """
    Profile Item Model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=250)
    work_description = models.TextField()
    Family_detail = models.TextField()
    user_Img = models.ImageField(upload_to='images/', default='Image is not here')

    def __str__(self):
        return self.nick_name

