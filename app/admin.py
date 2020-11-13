from django.contrib import admin
from app.models import Phone, OTP, Responses

class OTPAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display=('otp', 'created_at')

class ResponsesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display=('created_at', 'updated_at')

# Register your models here.
admin.site.register(Phone)
admin.site.register(Responses, ResponsesAdmin)
admin.site.register(OTP, OTPAdmin)
