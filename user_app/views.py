from django.contrib.auth import get_user_model, authenticate
# from .models import User
#from .permissions import IsAuthorOrReadOnly
from django.views.generic import ListView, TemplateView, CreateView, DetailView, View
from .forms import UserCreateForm
from django.urls import reverse_lazy, reverse
from rest_framework import viewsets # new
from . import forms
from django.contrib.auth import mixins
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
# Viewing Profile
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from app.models import Responses
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

import pandas as pd
import numpy as np
import json


class HomeView(TemplateView):
    template_name = 'user_app/index.html'


class SignUpView(CreateView):
    model = User
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('user_app:login')
    template_name = 'user_app/registration/sign_up.html'

    def register(request):
        registered = False
        if request.method == 'POST':

            user_form = UserCreateForm(data=request.POST)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user.password)

                user_form.save(commit=True)
                user.save()

                registered = True

            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserCreateForm()


class LogoutView(TemplateView):
    template_name = 'user_app/registration/logout_success.html'


@login_required
def dashboard(request):
    
    ##########################################################################################################################################
    # AGE
    age = 'age'
    age_queryset= list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))
    total_participants = Responses.objects.all().count()
    df = pd.DataFrame(age_queryset)
    conditions = [
    (df['age'] < 18),
    ((df['age']>=18)&(df['age']<=40)),
    ((df['age']>40)&(df['age']<=60)),
    (df['age'] > 60)
    ]
    values = ['< 18', '18 - 40', '41 - 60', '> 60']
    df['age_group'] = np.select(conditions, values)

    df_new=df.groupby('age_group').sum()
    queryset=df_new.to_dict()


    age_labels=[" < 18 years ", " 18 - 40 years ", " 41 - 60 years ", " > 60 years "]
    age_data=[]

    # for item in queryset['total'].keys():
    #     age_labels.append(item)
    for item in queryset['total'].values():
        age_data.append(item)

    # count
    query = list(Responses.objects.values(age))
    df = pd.DataFrame(query)
    age_response_count = list(df[df[age] != ""].count())[0]
    
    ##########################################################################################################################################
    # GENDER
    gender = 'gender'
    gender_queryset= list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    gender_labels=[]
    gender_data=[]

    for idx,item in enumerate(gender_queryset):
        gender_labels.append(gender_queryset[idx][gender])
        gender_data.append(gender_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(gender))
    df = pd.DataFrame(query)
    gender_response_count = list(df[df[gender] != ""].count())[0]    

    ##########################################################################################################################################
    marital_status = 'marital_status'
    marital_status_queryset= list(Responses.objects.all().values(marital_status).annotate(total=Count(marital_status)).order_by('total'))

    marital_status_labels=[]
    marital_status_data=[]

    for idx,item in enumerate(marital_status_queryset):
        marital_status_labels.append(marital_status_queryset[idx]['marital_status'])
        marital_status_data.append(marital_status_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(marital_status))
    df = pd.DataFrame(query)
    marital_response_count = list(df[df[marital_status] != ""].count())[0]    

    ##########################################################################################################################################
    religion = 'religion'
    religion_queryset= list(Responses.objects.all().values(religion).annotate(total=Count(religion)).order_by('total'))

    religion_labels=[]
    religion_data=[]

    for idx,item in enumerate(religion_queryset):
        religion_labels.append(religion_queryset[idx][religion])
        religion_data.append(religion_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(religion))
    df = pd.DataFrame(query)
    religion_response_count = list(df[df[religion] != ""].count())[0]     

    ##########################################################################################################################################
    job_type = 'job_type'
    job_type_queryset= list(Responses.objects.all().values(job_type).annotate(total=Count(job_type)).order_by('total'))

    job_type_labels=[]
    job_type_data=[]

    for idx,item in enumerate(job_type_queryset):
        job_type_labels.append(job_type_queryset[idx][job_type])
        job_type_data.append(job_type_queryset[idx]['total'])

     # count
    query = list(Responses.objects.values(job_type))
    df = pd.DataFrame(query)
    jobType_response_count = list(df[df[job_type] != ""].count())[0]  

    ##########################################################################################################################################
    job_category_health_related = 'job_category_health_related'
    job_category_health_related_queryset= list(Responses.objects.all().values(job_category_health_related).annotate(total=Count(job_category_health_related)).order_by('total'))

    job_category_health_related_labels=[]
    job_category_health_related_data=[]

    for idx,item in enumerate(job_category_health_related_queryset):
        job_category_health_related_labels.append(job_category_health_related_queryset[idx][job_category_health_related])
        job_category_health_related_data.append(job_category_health_related_queryset[idx]['total'])

     # count
    query = list(Responses.objects.values(job_category_health_related))
    df = pd.DataFrame(query)
    jobCategory_response_count = list(df[df[job_category_health_related] != ""].count())[0] 

    ##########################################################################################################################################

    clinical_or_nonclinical_job = 'clinical_or_nonclinical_job'
    clinical_or_nonclinical_job_queryset= list(Responses.objects.all().values(clinical_or_nonclinical_job).annotate(total=Count(clinical_or_nonclinical_job)).order_by('total'))

    clinical_or_nonclinical_job_labels=[]
    clinical_or_nonclinical_job_data=[]

    for idx,item in enumerate(clinical_or_nonclinical_job_queryset):
        clinical_or_nonclinical_job_labels.append(clinical_or_nonclinical_job_queryset[idx][clinical_or_nonclinical_job])
        clinical_or_nonclinical_job_data.append(clinical_or_nonclinical_job_queryset[idx]['total'])

     # count
    query = list(Responses.objects.values(clinical_or_nonclinical_job))
    df = pd.DataFrame(query)
    clinical_response_count = list(df[df[clinical_or_nonclinical_job] != ""].count())[0]

    ##########################################################################################################################################
    
    covid_knowledge_before_survey = 'covid_knowledge_before_survey'
    covid_knowledge_before_survey_queryset= list(Responses.objects.all().values(covid_knowledge_before_survey).annotate(total=Count(covid_knowledge_before_survey)).order_by('total'))

    covid_knowledge_before_survey_labels = []
    covid_knowledge_before_survey_data = []

    for idx,item in enumerate(covid_knowledge_before_survey_queryset):
        covid_knowledge_before_survey_labels.append(covid_knowledge_before_survey_queryset[idx][covid_knowledge_before_survey])
        covid_knowledge_before_survey_data.append(covid_knowledge_before_survey_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(covid_knowledge_before_survey))
    df = pd.DataFrame(query)
    covidKnowledge_response_count = list(df[df[covid_knowledge_before_survey] != ""].count())[0] 


    ##########################################################################################################################################

    risk_of_covid_exposure = 'risk_of_covid_exposure'
    risk_of_covid_exposure_queryset= list(Responses.objects.all().values(risk_of_covid_exposure).annotate(total=Count(risk_of_covid_exposure)).order_by('total'))

    risk_of_covid_exposure_labels=[]
    risk_of_covid_exposure_data=[]

    for idx,item in enumerate(risk_of_covid_exposure_queryset):
        risk_of_covid_exposure_labels.append(risk_of_covid_exposure_queryset[idx][risk_of_covid_exposure])
        risk_of_covid_exposure_data.append(risk_of_covid_exposure_queryset[idx]['total'])


    # count
    query = list(Responses.objects.values(risk_of_covid_exposure))
    df = pd.DataFrame(query)
    risk_response_count = list(df[df[risk_of_covid_exposure] != ""].count())[0] 

    ##########################################################################################################################################

    know_of_anyone_diagnosed_with_covid = 'know_of_anyone_diagnosed_with_covid'
    know_of_anyone_diagnosed_with_covid_queryset= list(Responses.objects.all().values(know_of_anyone_diagnosed_with_covid).annotate(total=Count(know_of_anyone_diagnosed_with_covid)).order_by('total'))

    know_of_anyone_diagnosed_with_covid_labels=[]
    know_of_anyone_diagnosed_with_covid_data=[]

    for idx,item in enumerate(know_of_anyone_diagnosed_with_covid_queryset):
        know_of_anyone_diagnosed_with_covid_labels.append(know_of_anyone_diagnosed_with_covid_queryset[idx][know_of_anyone_diagnosed_with_covid])
        know_of_anyone_diagnosed_with_covid_data.append(know_of_anyone_diagnosed_with_covid_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(know_of_anyone_diagnosed_with_covid))
    df = pd.DataFrame(query)
    diagnosed_response_count = list(df[df[know_of_anyone_diagnosed_with_covid] != ""].count())[0]

    ##########################################################################################################################################

    know_of_anyone_hospitalized_due_to_covid = 'know_of_anyone_hospitalized_due_to_covid'
    know_of_anyone_hospitalized_due_to_covid_queryset= list(Responses.objects.all().values(know_of_anyone_hospitalized_due_to_covid).annotate(total=Count(know_of_anyone_hospitalized_due_to_covid)).order_by('total'))

    know_of_anyone_hospitalized_due_to_covid_labels=[]
    know_of_anyone_hospitalized_due_to_covid_data=[]

    for idx,item in enumerate(know_of_anyone_hospitalized_due_to_covid_queryset):
        know_of_anyone_hospitalized_due_to_covid_labels.append(know_of_anyone_hospitalized_due_to_covid_queryset[idx][know_of_anyone_hospitalized_due_to_covid])
        know_of_anyone_hospitalized_due_to_covid_data.append(know_of_anyone_hospitalized_due_to_covid_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(know_of_anyone_hospitalized_due_to_covid))
    df = pd.DataFrame(query)
    hospitalized_response_count = list(df[df[know_of_anyone_hospitalized_due_to_covid] != ""].count())[0]

    ##########################################################################################################################################

    know_of_anyone_die_due_to_covid = 'know_of_anyone_die_due_to_covid'
    know_of_anyone_die_due_to_covid_queryset= list(Responses.objects.all().values(know_of_anyone_die_due_to_covid).annotate(total=Count(know_of_anyone_die_due_to_covid)).order_by('total'))

    know_of_anyone_die_due_to_covid_labels=[]
    know_of_anyone_die_due_to_covid_data=[]

    for idx,item in enumerate(know_of_anyone_die_due_to_covid_queryset):
        know_of_anyone_die_due_to_covid_labels.append(know_of_anyone_die_due_to_covid_queryset[idx][know_of_anyone_die_due_to_covid])
        know_of_anyone_die_due_to_covid_data.append(know_of_anyone_die_due_to_covid_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(know_of_anyone_die_due_to_covid))
    df = pd.DataFrame(query)
    die_response_count = list(df[df[know_of_anyone_die_due_to_covid] != ""].count())[0]

    ##########################################################################################################################################

    know_of_covid_preventive_measures = 'know_of_covid_preventive_measures'
    know_of_covid_preventive_measures_queryset= list(Responses.objects.all().values(know_of_covid_preventive_measures).annotate(total=Count(know_of_covid_preventive_measures)).order_by('total'))
    
    know_of_covid_preventive_measures_labels=[]
    know_of_covid_preventive_measures_data=[]

    for idx,item in enumerate(know_of_covid_preventive_measures_queryset):
        know_of_covid_preventive_measures_labels.append(know_of_covid_preventive_measures_queryset[idx][know_of_covid_preventive_measures])
        know_of_covid_preventive_measures_data.append(know_of_covid_preventive_measures_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(know_of_covid_preventive_measures))
    df = pd.DataFrame(query)
    preventive_response_count = list(df[df[know_of_covid_preventive_measures] != ""].count())[0]

    ##########################################################################################################################################

    believe_in_facemask_protection = 'believe_in_facemask_protection'
    believe_in_facemask_protection_queryset= list(Responses.objects.all().values(believe_in_facemask_protection).annotate(total=Count(believe_in_facemask_protection)).order_by('total'))

    believe_in_facemask_protection_labels=[]
    believe_in_facemask_protection_data=[]

    for idx,item in enumerate(believe_in_facemask_protection_queryset):
        believe_in_facemask_protection_labels.append(believe_in_facemask_protection_queryset[idx][believe_in_facemask_protection])
        believe_in_facemask_protection_data.append(believe_in_facemask_protection_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(believe_in_facemask_protection))
    df = pd.DataFrame(query)
    facemask_response_count = list(df[df[believe_in_facemask_protection] != ""].count())[0]

    ##########################################################################################################################################

    believe_in_social_distancing = 'believe_in_social_distancing'
    believe_in_social_distancing_queryset= list(Responses.objects.all().values(believe_in_social_distancing).annotate(total=Count(believe_in_social_distancing)).order_by('total'))

    believe_in_social_distancing_labels=[]
    believe_in_social_distancing_data=[]

    for idx,item in enumerate(believe_in_social_distancing_queryset):
        believe_in_social_distancing_labels.append(believe_in_social_distancing_queryset[idx][believe_in_social_distancing])
        believe_in_social_distancing_data.append(believe_in_social_distancing_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(believe_in_social_distancing))
    df = pd.DataFrame(query)
    social_response_count = list(df[df[believe_in_social_distancing] != ""].count())[0]   

    ##########################################################################################################################################

    believe_in_hand_washing = 'believe_in_hand_washing'
    believe_in_hand_washing_queryset= list(Responses.objects.all().values(believe_in_hand_washing).annotate(total=Count(believe_in_hand_washing)).order_by('total'))

    believe_in_hand_washing_labels=[]
    believe_in_hand_washing_data=[]

    for idx,item in enumerate(believe_in_hand_washing_queryset):
        believe_in_hand_washing_labels.append(believe_in_hand_washing_queryset[idx][believe_in_hand_washing])
        believe_in_hand_washing_data.append(believe_in_hand_washing_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(believe_in_hand_washing))
    df = pd.DataFrame(query)
    hand_response_count = list(df[df[believe_in_hand_washing] != ""].count())[0]

    ##########################################################################################################################################

    think_covid_is_gone = 'think_covid_is_gone'
    think_covid_is_gone_queryset= list(Responses.objects.all().values(think_covid_is_gone).annotate(total=Count(think_covid_is_gone)).order_by('total'))

    think_covid_is_gone_labels=[]
    think_covid_is_gone_data=[]

    for idx,item in enumerate(think_covid_is_gone_queryset):
        think_covid_is_gone_labels.append(think_covid_is_gone_queryset[idx][think_covid_is_gone])
        think_covid_is_gone_data.append(think_covid_is_gone_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(think_covid_is_gone))
    df = pd.DataFrame(query)
    gone_response_count = list(df[df[think_covid_is_gone] != ""].count())[0]

    ##########################################################################################################################################

    think_we_need_covid_vaccine = 'think_we_need_covid_vaccine'
    think_we_need_covid_vaccine_queryset= list(Responses.objects.all().values(think_we_need_covid_vaccine).annotate(total=Count(think_we_need_covid_vaccine)).order_by('total'))

    think_we_need_covid_vaccine_labels=[]
    think_we_need_covid_vaccine_data=[]

    for idx,item in enumerate(think_we_need_covid_vaccine_queryset):
        think_we_need_covid_vaccine_labels.append(think_we_need_covid_vaccine_queryset[idx][think_we_need_covid_vaccine])
        think_we_need_covid_vaccine_data.append(think_we_need_covid_vaccine_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(think_we_need_covid_vaccine))
    df = pd.DataFrame(query)
    need_response_count = list(df[df[think_we_need_covid_vaccine] != ""].count())[0]

    ##########################################################################################################################################
 
    think_vaccines_are_safe = 'think_vaccines_are_safe'
    think_vaccines_are_safe_queryset= list(Responses.objects.all().values(think_vaccines_are_safe).annotate(total=Count(think_vaccines_are_safe)).order_by('total'))

    think_vaccines_are_safe_labels=[]
    think_vaccines_are_safe_data=[]

    for idx,item in enumerate(think_vaccines_are_safe_queryset):
        think_vaccines_are_safe_labels.append(think_vaccines_are_safe_queryset[idx][think_vaccines_are_safe])
        think_vaccines_are_safe_data.append(think_vaccines_are_safe_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(think_vaccines_are_safe))
    df = pd.DataFrame(query)
    safe_response_count = list(df[df[think_vaccines_are_safe] != ""].count())[0]

    ##########################################################################################################################################

    heard_of_any_covid_candidate_vaccine = 'heard_of_any_covid_candidate_vaccine'
    heard_of_any_covid_candidate_vaccine_queryset= list(Responses.objects.all().values(heard_of_any_covid_candidate_vaccine).annotate(total=Count(heard_of_any_covid_candidate_vaccine)).order_by('total'))

    heard_of_any_covid_candidate_vaccine_labels=[]
    heard_of_any_covid_candidate_vaccine_data=[]

    for idx,item in enumerate(heard_of_any_covid_candidate_vaccine_queryset):
        heard_of_any_covid_candidate_vaccine_labels.append(heard_of_any_covid_candidate_vaccine_queryset[idx][heard_of_any_covid_candidate_vaccine])
        heard_of_any_covid_candidate_vaccine_data.append(heard_of_any_covid_candidate_vaccine_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(heard_of_any_covid_candidate_vaccine))
    df = pd.DataFrame(query)
    candidate_response_count = list(df[df[heard_of_any_covid_candidate_vaccine] != ""].count())[0]

    ##########################################################################################################################################

    participate_in_clinical_covid_vaccine_trial = 'participate_in_clinical_covid_vaccine_trial'
    participate_in_clinical_covid_vaccine_trial_queryset= list(Responses.objects.all().values(participate_in_clinical_covid_vaccine_trial).annotate(total=Count(participate_in_clinical_covid_vaccine_trial)).order_by('total'))

    participate_in_clinical_covid_vaccine_trial_labels=[]
    participate_in_clinical_covid_vaccine_trial_data=[]

    for idx,item in enumerate(heard_of_any_covid_candidate_vaccine_queryset):
        participate_in_clinical_covid_vaccine_trial_labels.append(participate_in_clinical_covid_vaccine_trial_queryset[idx][participate_in_clinical_covid_vaccine_trial])
        participate_in_clinical_covid_vaccine_trial_data.append(participate_in_clinical_covid_vaccine_trial_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(participate_in_clinical_covid_vaccine_trial))
    df = pd.DataFrame(query)
    trial_response_count = list(df[df[participate_in_clinical_covid_vaccine_trial] != ""].count())[0]

    ##########################################################################################################################################

    reason_not_to_participate_in_clinical_covid_vaccine_trial = 'reason_not_to_participate_in_clinical_covid_vaccine_trial'
    reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset= list(Responses.objects.all().values(reason_not_to_participate_in_clinical_covid_vaccine_trial).annotate(total=Count(reason_not_to_participate_in_clinical_covid_vaccine_trial)).order_by('total'))

    reason_not_to_participate_in_clinical_covid_vaccine_trial_labels=[]
    reason_not_to_participate_in_clinical_covid_vaccine_trial_data=[]

    for idx,item in enumerate(reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset):
        reason_not_to_participate_in_clinical_covid_vaccine_trial_labels.append(reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset[idx][reason_not_to_participate_in_clinical_covid_vaccine_trial])
        reason_not_to_participate_in_clinical_covid_vaccine_trial_data.append(reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(reason_not_to_participate_in_clinical_covid_vaccine_trial))
    df = pd.DataFrame(query)
    reason_response_count = list(df[df[reason_not_to_participate_in_clinical_covid_vaccine_trial] != ""].count())[0]

    ##########################################################################################################################################

    motivation_for_participation = 'motivation_for_participation'
    motivation_for_participation_queryset= list(Responses.objects.all().values(motivation_for_participation).annotate(total=Count(motivation_for_participation)).order_by('total'))

    motivation_for_participation_labels=[]
    motivation_for_participation_data=[]

    for idx,item in enumerate(motivation_for_participation_queryset):
        motivation_for_participation_labels.append(motivation_for_participation_queryset[idx][motivation_for_participation])
        motivation_for_participation_data.append(motivation_for_participation_queryset[idx]['total'])
    
    # count
    query = list(Responses.objects.values(motivation_for_participation))
    df = pd.DataFrame(query)
    motivation_response_count = list(df[df[motivation_for_participation] != ""].count())[0]
    
    ##########################################################################################################################################

    route_of_vaccine_administration = 'route_of_vaccine_administration'
    route_of_vaccine_administration_queryset= list(Responses.objects.all().values(route_of_vaccine_administration).annotate(total=Count(route_of_vaccine_administration)).order_by('total'))

    route_of_vaccine_administration_labels=[]
    route_of_vaccine_administration_data=[]

    for idx,item in enumerate(route_of_vaccine_administration_queryset):
        route_of_vaccine_administration_labels.append(route_of_vaccine_administration_queryset[idx][route_of_vaccine_administration])
        route_of_vaccine_administration_data.append(route_of_vaccine_administration_queryset[idx]['total'])

     # count
    query = list(Responses.objects.values(route_of_vaccine_administration))
    df = pd.DataFrame(query)
    route_response_count = list(df[df[route_of_vaccine_administration] != ""].count())[0]

    ##########################################################################################################################################

    type_of_vaccine_acceptable = 'type_of_vaccine_acceptable'
    type_of_vaccine_acceptable_queryset= list(Responses.objects.all().values(type_of_vaccine_acceptable).annotate(total=Count(type_of_vaccine_acceptable)).order_by('total'))

    type_of_vaccine_acceptable_labels=[]
    type_of_vaccine_acceptable_data=[]

    for idx,item in enumerate(type_of_vaccine_acceptable_queryset):
        type_of_vaccine_acceptable_labels.append(type_of_vaccine_acceptable_queryset[idx][type_of_vaccine_acceptable])
        type_of_vaccine_acceptable_data.append(type_of_vaccine_acceptable_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(type_of_vaccine_acceptable))
    df = pd.DataFrame(query)
    vaccType_response_count = list(df[df[type_of_vaccine_acceptable] != ""].count())[0]

    ##########################################################################################################################################

    phase_of_clinical_trial_to_participate_in = 'phase_of_clinical_trial_to_participate_in'
    phase_of_clinical_trial_to_participate_in_queryset= list(Responses.objects.all().values(phase_of_clinical_trial_to_participate_in).annotate(total=Count(phase_of_clinical_trial_to_participate_in)).order_by('total'))

    phase_of_clinical_trial_to_participate_in_labels=[]
    phase_of_clinical_trial_to_participate_in_data=[]

    for idx,item in enumerate(phase_of_clinical_trial_to_participate_in_queryset):
        phase_of_clinical_trial_to_participate_in_labels.append(phase_of_clinical_trial_to_participate_in_queryset[idx][phase_of_clinical_trial_to_participate_in])
        phase_of_clinical_trial_to_participate_in_data.append(phase_of_clinical_trial_to_participate_in_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(phase_of_clinical_trial_to_participate_in))
    df = pd.DataFrame(query)
    phase_response_count = list(df[df[phase_of_clinical_trial_to_participate_in] != ""].count())[0]

    ##########################################################################################################################################

    country_of_vaccine_influence_your_decision_to_participate = 'country_of_vaccine_influence_your_decision_to_participate'
    country_of_vaccine_influence_your_decision_to_participate_queryset= list(Responses.objects.all().values(country_of_vaccine_influence_your_decision_to_participate).annotate(total=Count(country_of_vaccine_influence_your_decision_to_participate)).order_by('total'))

    country_of_vaccine_influence_your_decision_to_participate_labels=[]
    country_of_vaccine_influence_your_decision_to_participate_data=[]

    for idx,item in enumerate(country_of_vaccine_influence_your_decision_to_participate_queryset):
        country_of_vaccine_influence_your_decision_to_participate_labels.append(country_of_vaccine_influence_your_decision_to_participate_queryset[idx][country_of_vaccine_influence_your_decision_to_participate])
        country_of_vaccine_influence_your_decision_to_participate_data.append(country_of_vaccine_influence_your_decision_to_participate_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(country_of_vaccine_influence_your_decision_to_participate))
    df = pd.DataFrame(query)
    vaccCountry_response_count = list(df[df[country_of_vaccine_influence_your_decision_to_participate] != ""].count())[0]

    ##########################################################################################################################################

    preferred_vaccine_continent = 'preferred_vaccine_continent'
    preferred_vaccine_continent_queryset= list(Responses.objects.all().values(preferred_vaccine_continent).annotate(total=Count(preferred_vaccine_continent)).order_by('total'))

    preferred_vaccine_continent_labels=[]
    preferred_vaccine_continent_data=[]

    for idx,item in enumerate(preferred_vaccine_continent_queryset):
        preferred_vaccine_continent_labels.append(preferred_vaccine_continent_queryset[idx][preferred_vaccine_continent])
        preferred_vaccine_continent_data.append(preferred_vaccine_continent_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(preferred_vaccine_continent))
    df = pd.DataFrame(query)
    vaccContinent_response_count = list(df[df[preferred_vaccine_continent] != ""].count())[0]

    ##########################################################################################################################################

    vaccine_scientists_should_include_ghanaian = 'vaccine_scientists_should_include_ghanaian'
    vaccine_scientists_should_include_ghanaian_queryset= list(Responses.objects.all().values(vaccine_scientists_should_include_ghanaian).annotate(total=Count(vaccine_scientists_should_include_ghanaian)).order_by('total'))

    vaccine_scientists_should_include_ghanaian_labels=[]
    vaccine_scientists_should_include_ghanaian_data=[]

    for idx,item in enumerate(vaccine_scientists_should_include_ghanaian_queryset):
        vaccine_scientists_should_include_ghanaian_labels.append(vaccine_scientists_should_include_ghanaian_queryset[idx][vaccine_scientists_should_include_ghanaian])
        vaccine_scientists_should_include_ghanaian_data.append(vaccine_scientists_should_include_ghanaian_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(vaccine_scientists_should_include_ghanaian))
    df = pd.DataFrame(query)
    gh_response_count = list(df[df[vaccine_scientists_should_include_ghanaian] != ""].count())[0]

    ##########################################################################################################################################

    participate_in_mass_covid_vaccination = 'participate_in_mass_covid_vaccination'
    participate_in_mass_covid_vaccination_queryset= list(Responses.objects.all().values(participate_in_mass_covid_vaccination).annotate(total=Count(participate_in_mass_covid_vaccination)).order_by('total'))

    participate_in_mass_covid_vaccination_labels=[]
    participate_in_mass_covid_vaccination_data=[]

    for idx,item in enumerate(participate_in_mass_covid_vaccination_queryset):
        participate_in_mass_covid_vaccination_labels.append(participate_in_mass_covid_vaccination_queryset[idx][participate_in_mass_covid_vaccination])
        participate_in_mass_covid_vaccination_data.append(participate_in_mass_covid_vaccination_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(participate_in_mass_covid_vaccination))
    df = pd.DataFrame(query)
    mass_response_count = list(df[df[participate_in_mass_covid_vaccination] != ""].count())[0]

    ##########################################################################################################################################

    prepared_to_pay_for_vaccine = 'prepared_to_pay_for_vaccine'
    prepared_to_pay_for_vaccine_queryset= list(Responses.objects.all().values(prepared_to_pay_for_vaccine).annotate(total=Count(prepared_to_pay_for_vaccine)).order_by('total'))

    prepared_to_pay_for_vaccine_labels=[]
    prepared_to_pay_for_vaccine_data=[]

    for idx,item in enumerate(prepared_to_pay_for_vaccine_queryset):
        prepared_to_pay_for_vaccine_labels.append(prepared_to_pay_for_vaccine_queryset[idx][prepared_to_pay_for_vaccine])
        prepared_to_pay_for_vaccine_data.append(prepared_to_pay_for_vaccine_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(prepared_to_pay_for_vaccine))
    df = pd.DataFrame(query)
    pay_response_count = list(df[df[prepared_to_pay_for_vaccine] != ""].count())[0]

    ##########################################################################################################################################

    estimated_vaccine_cost_range = 'estimated_vaccine_cost_range'
    estimated_vaccine_cost_range_queryset= list(Responses.objects.all().values(estimated_vaccine_cost_range).annotate(total=Count(estimated_vaccine_cost_range)).order_by('total'))

    estimated_vaccine_cost_range_labels=[]
    estimated_vaccine_cost_range_data=[]

    for idx,item in enumerate(estimated_vaccine_cost_range_queryset):
        estimated_vaccine_cost_range_labels.append(estimated_vaccine_cost_range_queryset[idx][estimated_vaccine_cost_range])
        estimated_vaccine_cost_range_data.append(estimated_vaccine_cost_range_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(estimated_vaccine_cost_range))
    df = pd.DataFrame(query)
    cost_response_count = list(df[df[estimated_vaccine_cost_range] != ""].count())[0]

    ##########################################################################################################################################

    origin_of_vaccine_influence_your_decision_to_participate = 'origin_of_vaccine_influence_your_decision_to_participate'
    origin_of_vaccine_influence_your_decision_to_participate_queryset= list(Responses.objects.all().values(origin_of_vaccine_influence_your_decision_to_participate).annotate(total=Count(origin_of_vaccine_influence_your_decision_to_participate)).order_by('total'))

    origin_of_vaccine_influence_your_decision_to_participate_labels=[]
    origin_of_vaccine_influence_your_decision_to_participate_data=[]

    for idx,item in enumerate(origin_of_vaccine_influence_your_decision_to_participate_queryset):
        origin_of_vaccine_influence_your_decision_to_participate_labels.append(origin_of_vaccine_influence_your_decision_to_participate_queryset[idx][origin_of_vaccine_influence_your_decision_to_participate])
        origin_of_vaccine_influence_your_decision_to_participate_data.append(origin_of_vaccine_influence_your_decision_to_participate_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(origin_of_vaccine_influence_your_decision_to_participate))
    df = pd.DataFrame(query)
    origin_response_count = list(df[df[origin_of_vaccine_influence_your_decision_to_participate] != ""].count())[0]

    ##########################################################################################################################################

    preferred_vaccine_origin = 'preferred_vaccine_origin'
    preferred_vaccine_origin_queryset= list(Responses.objects.all().values(preferred_vaccine_origin).annotate(total=Count(preferred_vaccine_origin)).order_by('total'))

    preferred_vaccine_origin_labels=[]
    preferred_vaccine_origin_data=[]

    for idx,item in enumerate(preferred_vaccine_origin_queryset):
        preferred_vaccine_origin_labels.append(preferred_vaccine_origin_queryset[idx][preferred_vaccine_origin])
        preferred_vaccine_origin_data.append(preferred_vaccine_origin_queryset[idx]['total'])

    # count
    query = list(Responses.objects.values(preferred_vaccine_origin))
    df = pd.DataFrame(query)
    preferredOrigin_response_count = list(df[df[preferred_vaccine_origin] != ""].count())[0]
    
    ##########################################################################################################################################


    return render(request, 'charts/index.html', {
        'gender_labels': gender_labels,
        'gender_data': gender_data,

        'age_labels': age_labels,
        'age_data': age_data,

        'marital_status_labels': marital_status_labels,
        'marital_status_data': marital_status_data,

        'religion_labels': religion_labels,
        'religion_data': religion_data,

        'job_type_labels': job_type_labels,
        'job_type_data': job_type_data,

        'job_category_health_related_labels': job_category_health_related_labels,
        'job_category_health_related_data': job_category_health_related_data,

        'clinical_or_nonclinical_job_labels': clinical_or_nonclinical_job_labels,
        'clinical_or_nonclinical_job_data': clinical_or_nonclinical_job_data,
        
        'covid_knowledge_before_survey_labels':covid_knowledge_before_survey_labels,
        'covid_knowledge_before_survey_data':covid_knowledge_before_survey_data,

        'risk_of_covid_exposure_labels':risk_of_covid_exposure_labels,
        'risk_of_covid_exposure_data': risk_of_covid_exposure_data,

        'know_of_anyone_diagnosed_with_covid_labels': know_of_anyone_diagnosed_with_covid_labels,
        'know_of_anyone_diagnosed_with_covid_data': know_of_anyone_diagnosed_with_covid_data,

        'know_of_anyone_hospitalized_due_to_covid_labels': know_of_anyone_hospitalized_due_to_covid_labels,
        'know_of_anyone_hospitalized_due_to_covid_data': know_of_anyone_hospitalized_due_to_covid_data,

        'know_of_anyone_die_due_to_covid_labels': know_of_anyone_die_due_to_covid_labels,
        'know_of_anyone_die_due_to_covid_data': know_of_anyone_die_due_to_covid_data,

        'know_of_covid_preventive_measures_labels': know_of_covid_preventive_measures_labels,
        'know_of_covid_preventive_measures_data': know_of_covid_preventive_measures_data,

        'believe_in_facemask_protection_labels': believe_in_facemask_protection_labels,
        'believe_in_facemask_protection_data': believe_in_facemask_protection_data,

        'believe_in_social_distancing_labels': believe_in_social_distancing_labels,
        'believe_in_social_distancing_data': believe_in_social_distancing_data,

        'believe_in_hand_washing_labels': believe_in_hand_washing_labels,
        'believe_in_hand_washing_data': believe_in_hand_washing_data,

        'think_covid_is_gone_labels': think_covid_is_gone_labels,
        'think_covid_is_gone_data': think_covid_is_gone_data,

        'think_we_need_covid_vaccine_labels': think_we_need_covid_vaccine_labels,
        'think_we_need_covid_vaccine_data': think_we_need_covid_vaccine_data,

        'think_vaccines_are_safe_labels': think_vaccines_are_safe_labels,
        'think_vaccines_are_safe_data': think_vaccines_are_safe_data,

        'heard_of_any_covid_candidate_vaccine_labels':heard_of_any_covid_candidate_vaccine_labels,
        'heard_of_any_covid_candidate_vaccine_data': heard_of_any_covid_candidate_vaccine_data,

        'participate_in_clinical_covid_vaccine_trial_labels': participate_in_clinical_covid_vaccine_trial_labels,
        'participate_in_clinical_covid_vaccine_trial_data': participate_in_clinical_covid_vaccine_trial_data,

        'reason_not_to_participate_in_clinical_covid_vaccine_trial_data': reason_not_to_participate_in_clinical_covid_vaccine_trial_data,
        'reason_not_to_participate_in_clinical_covid_vaccine_trial_labels': reason_not_to_participate_in_clinical_covid_vaccine_trial_labels,

        'motivation_for_participation_labels': motivation_for_participation_labels,
        'motivation_for_participation_data': motivation_for_participation_data,

        'route_of_vaccine_administration_labels': route_of_vaccine_administration_labels,
        'route_of_vaccine_administration_data': route_of_vaccine_administration_data,

        'type_of_vaccine_acceptable_labels': type_of_vaccine_acceptable_labels,
        'type_of_vaccine_acceptable_data': type_of_vaccine_acceptable_data,

        'phase_of_clinical_trial_to_participate_in_labels': phase_of_clinical_trial_to_participate_in_labels,
        'phase_of_clinical_trial_to_participate_in_data':phase_of_clinical_trial_to_participate_in_data,

        'country_of_vaccine_influence_your_decision_to_participate_labels': country_of_vaccine_influence_your_decision_to_participate_labels,
        'country_of_vaccine_influence_your_decision_to_participate_data': country_of_vaccine_influence_your_decision_to_participate_data,       

        'preferred_vaccine_continent_labels': preferred_vaccine_continent_labels,
        'preferred_vaccine_continent_data': preferred_vaccine_continent_data,

        'vaccine_scientists_should_include_ghanaian_labels': vaccine_scientists_should_include_ghanaian_labels,
        'vaccine_scientists_should_include_ghanaian_data': vaccine_scientists_should_include_ghanaian_data,

        'participate_in_mass_covid_vaccination_labels': participate_in_mass_covid_vaccination_labels,
        'participate_in_mass_covid_vaccination_data': participate_in_mass_covid_vaccination_data,

        'prepared_to_pay_for_vaccine_labels': prepared_to_pay_for_vaccine_labels,
        'prepared_to_pay_for_vaccine_data': prepared_to_pay_for_vaccine_data,

        'estimated_vaccine_cost_range_labels': estimated_vaccine_cost_range_labels,
        'estimated_vaccine_cost_range_data': estimated_vaccine_cost_range_data,

        'origin_of_vaccine_influence_your_decision_to_participate_labels': origin_of_vaccine_influence_your_decision_to_participate_labels,
        'origin_of_vaccine_influence_your_decision_to_participate_data': origin_of_vaccine_influence_your_decision_to_participate_data,

        'preferred_vaccine_origin_labels': preferred_vaccine_origin_labels,
        'preferred_vaccine_origin_data': preferred_vaccine_origin_data,

        'total_participants': total_participants,
        'query': query,

        ###############################################################################################
        
        'age_response_count': age_response_count,
        'gender_response_count': gender_response_count,
        'marital_response_count': marital_response_count,
        'religion_response_count': religion_response_count,
        'jobType_response_count':jobType_response_count,
        'jobCategory_response_count': jobCategory_response_count,
        'clinical_response_count': clinical_response_count,
        'covidKnowledge_response_count': covidKnowledge_response_count,
        'risk_response_count': risk_response_count,
        'diagnosed_response_count': diagnosed_response_count,
        'hospitalized_response_count': hospitalized_response_count,
        'die_response_count': die_response_count,
        'preventive_response_count': preventive_response_count,
        'facemask_response_count': facemask_response_count,
        'social_response_count': social_response_count,
        'hand_response_count': hand_response_count,
        'gone_response_count': gone_response_count,
        'need_response_count': need_response_count,
        'safe_response_count': safe_response_count,
        'candidate_response_count': candidate_response_count,
        'trial_response_count': trial_response_count,
        'reason_response_count': reason_response_count,
        'motivation_response_count': motivation_response_count,
        'route_response_count': route_response_count,
        'vaccType_response_count': vaccType_response_count,
        'phase_response_count': phase_response_count,
        'vaccCountry_response_count': vaccCountry_response_count,
        'vaccContinent_response_count': vaccContinent_response_count,
        'gh_response_count': gh_response_count,
        'mass_response_count': mass_response_count,
        'pay_response_count': pay_response_count,
        'cost_response_count': cost_response_count,
        'origin_response_count': origin_response_count,
        'preferredOrigin_response_count': preferredOrigin_response_count

    })
   
   


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.is_active = True
    user.save()

    return redirect('login')


