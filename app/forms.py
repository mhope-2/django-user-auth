from django import forms
from .models import Phone, OTP

class PhoneForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Contact', 'size':'12', 'class': "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = True
        
    class Meta:
        verbose_name = 'Phone Number'
        fields = ['phone']

class OTPForm(forms.ModelForm):
    otp = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter OTP', 'size':'12', 'class': "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['otp'].required = True
        
    class Meta:
        verbose_name = 'OTP'
        model = OTP
        fields = ['otp']