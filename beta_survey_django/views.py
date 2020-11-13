from django.shortcuts import render, redirect
import requests 
from app.forms import PhoneForm, OTPForm
from app.models import Phone, OTP
import uuid
import random
from random import shuffle
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    headers = {"Content-Type":"application/json", "Accept":"application/json",  "Access-Control-Allow-Origin":"https://cors-anywhere.herokuapp.com/https://ipleak.net/json/",
    "Access-Control-Allow-Credentials":"true"}

    if request.method == 'POST':
        form = PhoneForm(request.POST)
        model = Phone
        if form.is_valid():
            phone = form.cleaned_data['phone']
            form.save()
            # send SMS
            deywuro_sms = "https://deywuro.com/api/sms"
            gen_otp=str(random.Random(uuid.uuid1().hex).getrandbits(128))[0:6]
            params = {
                    "username": "sammy",
                    "password": "suppORT_pass_0987",
                    "source": "Test",
                    "destination": "{}".format(str(phone)),
                    "message": "Your OTP is {}".format(gen_otp)
            }
            deywuro_request = requests.get(url = deywuro_sms, params = params, headers = {"Content-Type":"application/json"})   
            otp_save = OTP(otp=gen_otp)
            otp_save.save()

            data = deywuro_request.json()
            print("SMS RESPONSE", data)
            return redirect('verify_otp')
    else:
        form = PhoneForm()

    # location
    url = 'https://ipleak.net/json/'
    # sending get request and saving the response as response object 
    location_request = requests.get(url = url, headers = headers) 
    data = location_request.json()
    if(data['country_name'] == "Ghana"):
        print("YOU ARE IN GHANA")
    else:
        return redirect('forbidden')
    return render(request, 'app/index.html',  {'form':form})


def verify_otp(request):

    if request.method == 'POST':
        form = OTPForm(request.POST)
        model = OTP        

        if form.is_valid():
            request.session["fav_color"] = "blue"
            fav_color = request.session["fav_color"]
            request.session.set_expiry(900)
            user_otp = form.cleaned_data['otp']
            otp_check = OTP.objects.filter(otp = user_otp).count()
            if otp_check > 0 and "fav_color" in request.session:
                print("FAV COLOR",fav_color)
                return redirect('survey')
            else:
                return redirect('index')
        else:
            return redirect('index')
    else:
        form = OTPForm()

    return render(request, 'app/verify.html', {'form':form})


def survey(request):

    if "fav_color" not in request.session:
        return redirect('index')
    else:
        return render(request, 'app/survey.html')
        
        del request.session['fav_color']
    del request.session['fav_color']


def forbidden(request):
    return render(request, 'app/forbidden.html')
