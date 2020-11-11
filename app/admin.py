from django.contrib import admin
from app.models import Phone, OTP

class OTPAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display=('otp', 'submitted_at')

# Register your models here.
admin.site.register(Phone)
admin.site.register(OTP, OTPAdmin)