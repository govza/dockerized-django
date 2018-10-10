from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            UserProfile.objects.create(user=self)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile')

    department = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, default="CH")
    work_rate = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=100)
    trained = models.BooleanField(default=True)
    emp_id = models.CharField(max_length=255, blank=True)
    emp_type = models.CharField(max_length=255, blank=True)
    started = models.DateField(default=date(2000, 1, 1))
    ended = models.DateField(default=date(2030, 1, 1))

    def __str__(self):
        return 'Profile for user {}'.format(self.user.name)
