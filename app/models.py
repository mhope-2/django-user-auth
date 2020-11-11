from django.db import models
from django.utils import timezone

# Create your models here.
class Phone(models.Model):
    phone = models.CharField(max_length=12)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = "phone"
        verbose_name_plural = "phones"

class OTP(models.Model):
    id = models.IntegerField(primary_key=True)
    otp = models.CharField(max_length=6)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.otp)

    class Meta:
        verbose_name = "otp"
        verbose_name_plural = "otps"
