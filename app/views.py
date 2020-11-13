from django.shortcuts import render, redirect
from app.models import Responses
# API VIEW
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from datetime import datetime, timedelta
from app.serializers import ResponseSerializer
from django.views.decorators.csrf import csrf_exempt
from beta_survey_django import views
from rest_framework.reverse import reverse_lazy
import uuid
import logging
import json

from django.db.models import Count
from app.models import Responses

# api view
log_path = settings.MEDIA_ROOT + '/logs/response.log'
logging.basicConfig(filename=log_path,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.DEBUG)

# @csrf_exempt
@api_view(['GET', 'POST'])
def response_api(request):

    if request.method == 'POST':
        print("POST REQUEST")
        # religion other
        if request.data['religion'] == 'Other':
            religion = request.data['religion_other']
        else:
            religion = request.data['religion']

        # rel other undefined
        if request.data['religion_other'] == "undefined":
            request.data['religion_other'] = ""

        # job type other
        if request.data['job_type'] == 'Other':
            job_type = request.data['job_type_other']
        else:
            job_type = request.data['job_type']

        # job type other undefined
        if request.data['job_type_other'] == "undefined":
            request.data['job_type_other'] = ""

        # reason not to participate other
        if request.data['reason_not_to_participate_in_clinical_covid_vaccine_trial'] == "Other":
            reason_not_to_participate_in_clinical_covid_vaccine_trial = request.data['reason_not_to_participate_in_clinical_covid_vaccine_trial_other']
        else:
            reason_not_to_participate_in_clinical_covid_vaccine_trial = request.data['reason_not_to_participate_in_clinical_covid_vaccine_trial']

        # reason undefined
        if request.data['reason_not_to_participate_in_clinical_covid_vaccine_trial_other'] == "undefined":
            request.data['reason_not_to_participate_in_clinical_covid_vaccine_trial_other'] = ""

        responses = Responses.objects.all()
        serializer = ResponseSerializer(data=request.data)

        if serializer.is_valid():
            print("SERIALIZER VALID")
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            print("INVALID")

    elif request.method == 'GET':
        return Response({"my_msg":"use post instead"}, status=status.HTTP_201_CREATED)



def submitted(request):

    return render(request, 'app/submitted.html')