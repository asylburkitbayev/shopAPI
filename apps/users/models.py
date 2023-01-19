from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Libraries for signal

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Libraries for QR Code

from io import BytesIO
import qrcode
from PIL import Image, ImageDraw
from django.core.files import File


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='Номер телефона')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    code = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    cashback_all = models.DecimalField(max_digits=10, decimal_places=2,
                                       validators=[MinValueValidator(0)], default=0)

    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'is_seller']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} {self.email} {self.phone}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        qrcode_img = qrcode.make('{"user_id": "%s"}' % self.pk)
        canvas = Image.new('RGB', (330, 330), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        file_name = f'qr_code-{self.username}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save()


# signal for create Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
