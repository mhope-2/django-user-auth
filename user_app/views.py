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

    age_labels=[]
    age_data=[]

    for idx,item in enumerate(age_queryset):
        age_labels.append(age_queryset[idx][age])
        age_labels.append(age_queryset[idx]['total'])
    
    ##########################################################################################################################################
    # GENDER
    gender = 'gender'
    gender_queryset= list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    gender_labels=[]
    gender_data=[]

    for idx,item in enumerate(gender_queryset):
        gender_labels.append(gender_queryset[idx][gender])
        gender_data.append(gender_queryset[idx]['total'])

    ##########################################################################################################################################
    marital_status = 'marital_status'
    marital_status_queryset= list(Responses.objects.all().values(marital_status).annotate(total=Count(marital_status)).order_by('total'))

    marital_status_labels=[]
    marital_status_data=[]

    for idx,item in enumerate(marital_status_queryset):
        labels.append(marital_status_queryset[idx][marital_status])
        data.append(marital_status_queryset[idx]['total'])

    ##########################################################################################################################################
    religion = 'religion'
    religion_queryset= list(Responses.objects.all().values(religion).annotate(total=Count(religion)).order_by('total'))

    religion_labels=[]
    religion_data=[]

    for idx,item in enumerate(religion_queryset):
        labels.append(religion_queryset[idx][religion])
        data.append(religion_queryset[idx]['total'])

    ##########################################################################################################################################
    job_type = 'job_type'
    job_type_queryset= list(Responses.objects.all().values(job_type).annotate(total=Count(job_type)).order_by('total'))

    job_type_labels=[]
    job_type_data=[]

    for idx,item in enumerate(job_type_queryset):
        job_type_labels.append(job_type_queryset[idx][religion])
        job_type_data.append(job_type_queryset[idx]['total'])

    ##########################################################################################################################################
    job_category_health_related = 'job_category_health_related'
    job_category_health_related_queryset= list(Responses.objects.all().values(job_category_health_related).annotate(total=Count(job_category_health_related)).order_by('total'))

    job_category_health_related_labels=[]
    job_category_health_related_data=[]

    for idx,item in enumerate(job_type_queryset):
        job_category_health_related_labels.append(job_category_health_related_queryset[idx][job_category_health_related])
        job_category_health_related_data.append(job_category_health_related_queryset[idx]['total'])

    ##########################################################################################################################################

    clinical_or_nonclinical_job = 'clinical_or_nonclinical_job'
    clinical_or_nonclinical_job_queryset= list(Responses.objects.all().values(clinical_or_nonclinical_job).annotate(total=Count(clinical_or_nonclinical_job)).order_by('total'))

    job_category_health_related_labels=[]
    job_category_health_related_data=[]

    for idx,item in enumerate(clinical_or_nonclinical_job_queryset):
        clinical_or_nonclinical_job_labels.append(clinical_or_nonclinical_job_queryset[idx][clinical_or_nonclinical_job])
        clinical_or_nonclinical_job_data.append(clinical_or_nonclinical_job_queryset[idx]['total'])

    ##########################################################################################################################################
    
    covid_knowledge_before_survey = 'covid_knowledge_before_survey'
    covid_knowledge_before_survey_queryset= list(Responses.objects.all().values(covid_knowledge_before_survey).annotate(total=Count(covid_knowledge_before_survey)).order_by('total'))

    job_category_health_related_labels=[]
    job_category_health_related_data=[]

    for idx,item in enumerate(covid_knowledge_before_survey_queryset):
        covid_knowledge_before_survey_labels.append(covid_knowledge_before_survey_queryset[idx][covid_knowledge_before_survey])
        covid_knowledge_before_survey_data.append(covid_knowledge_before_survey_queryset[idx]['total'])

    ##########################################################################################################################################

    risk_of_covid_exposure = 'risk_of_covid_exposure'
    risk_of_covid_exposure_queryset= list(Responses.objects.all().values(risk_of_covid_exposure).annotate(total=Count(risk_of_covid_exposure)).order_by('total'))

    job_category_health_related_labels=[]
    job_category_health_related_data=[]

    for idx,item in enumerate(risk_of_covid_exposure_queryset):
        covid_knowledge_before_survey_labels.append(risk_of_covid_exposure_queryset[idx][risk_of_covid_exposure])
        covid_knowledge_before_survey_data.append(risk_of_covid_exposure_queryset[idx]['total'])

    ##########################################################################################################################################

    know_of_anyone_diagnosed_with_covid = 'know_of_anyone_diagnosed_with_covid'
    know_of_anyone_diagnosed_with_covid_queryset= list(Responses.objects.all().values(know_of_anyone_diagnosed_with_covid).annotate(total=Count(know_of_anyone_diagnosed_with_covid)).order_by('total'))

    risk_of_covid_exposure = 'risk_of_covid_exposure'
    risk_of_covid_exposure_queryset= list(Responses.objects.all().values(risk_of_covid_exposure).annotate(total=Count(risk_of_covid_exposure)).order_by('total'))

    covid_knowledge_before_survey_labels=[]
    covid_knowledge_before_survey_data=[]

    for idx,item in enumerate(know_of_anyone_diagnosed_with_covid_queryset):
        covid_knowledge_before_survey_labels.append(risk_of_covid_exposure_queryset[idx][risk_of_covid_exposure])
        covid_knowledge_before_survey_data.append(risk_of_covid_exposure_queryset[idx]['total'])

    ##########################################################################################################################################

    know_of_anyone_hospitalized_due_to_covid = 'know_of_anyone_hospitalized_due_to_covid'
    know_of_anyone_hospitalized_due_to_covid_queryset= list(Responses.objects.all().values(know_of_anyone_hospitalized_due_to_covid).annotate(total=Count(know_of_anyone_hospitalized_due_to_covid)).order_by('total'))

    know_of_anyone_hospitalized_due_to_covid_labels=[]
    know_of_anyone_hospitalized_due_to_covid_data=[]

    for idx,item in enumerate(know_of_anyone_hospitalized_due_to_covid_queryset):
        know_of_anyone_hospitalized_due_to_covid_labels.append(risk_of_covid_exposure_queryset[idx][know_of_anyone_hospitalized_due_to_covid])
        know_of_anyone_hospitalized_due_to_covid_data.append(risk_of_covid_exposure_queryset[idx]['total'])

    ##########################################################################################################################################

    know_of_anyone_die_due_to_covid = 'know_of_anyone_die_due_to_covid'
    know_of_anyone_die_due_to_covid_queryset= list(Responses.objects.all().values(know_of_anyone_die_due_to_covid).annotate(total=Count(know_of_anyone_die_due_to_covid)).order_by('total'))

    know_of_anyone_die_due_to_covid_covid_labels=[]
    know_of_anyone_die_due_to_covid_data=[]

    for idx,item in enumerate(know_of_anyone_die_due_to_covid_queryset):
        know_of_anyone_die_due_to_covid_labels.append(risk_of_covid_exposure_queryset[idx][know_of_anyone_hospitalized_due_to_covid])
        know_of_anyone_die_due_to_covid_data.append(risk_of_covid_exposure_queryset[idx]['total'])

    ##########################################################################################################################################

    know_of_covid_preventive_measures = 'know_of_covid_preventive_measures'
    know_of_covid_preventive_measures_queryset= list(Responses.objects.all().values(know_of_covid_preventive_measures).annotate(total=Count(know_of_covid_preventive_measures)).order_by('total'))
    
    know_of_anyone_hospitalized_due_to_covid_labels=[]
    know_of_anyone_hospitalized_due_to_covid_data=[]

    for idx,item in enumerate(know_of_anyone_die_due_to_covid_queryset):
        know_of_anyone_hospitalized_due_to_covid_labels.append(know_of_anyone_die_due_to_covid_queryset[idx][know_of_anyone_hospitalized_due_to_covid])
        know_of_anyone_hospitalized_due_to_covid_data.append(risk_of_covid_exposure_queryset[idx]['total'])

    ##########################################################################################################################################

    believe_in_facemask_protection = 'believe_in_facemask_protection'
    believe_in_facemask_protection_queryset= list(Responses.objects.all().values(believe_in_facemask_protection).annotate(total=Count(believe_in_facemask_protection)).order_by('total'))

    believe_in_facemask_protection_labels=[]
    believe_in_facemask_protection_data=[]

    for idx,item in enumerate(believe_in_facemask_protection_queryset):
        believe_in_facemask_protection_labels.append(believe_in_facemask_protection_queryset[idx][know_of_anyone_hospitalized_due_to_covid])
        believe_in_facemask_protection_data.append(believe_in_facemask_protection_queryset[idx]['total'])

    ##########################################################################################################################################

    believe_in_social_distancing = 'believe_in_social_distancing'
    believe_in_social_distancing_queryset= list(Responses.objects.all().values(believe_in_social_distancing).annotate(total=Count(believe_in_social_distancing)).order_by('total'))

    believe_in_social_distancing_labels=[]
    believe_in_social_distancing_data=[]

    for idx,item in enumerate(believe_in_social_distancing_queryset):
        believe_in_social_distancing_labels.append(believe_in_social_distancing_queryset[idx][know_of_anyone_hospitalized_due_to_covid])
        believe_in_social_distancing_data.append(believe_in_social_distancing_queryset[idx]['total'])

    ##########################################################################################################################################

    believe_in_hand_washing = 'believe_in_hand_washing'
    believe_in_hand_washing_queryset= list(Responses.objects.all().values(believe_in_hand_washing).annotate(total=Count(believe_in_hand_washing)).order_by('total'))

    believe_in_hand_washing_labels=[]
    believe_in_hand_washing_data=[]

    for idx,item in enumerate(believe_in_hand_washing_queryset):
        believe_in_hand_washing_labels.append(believe_in_hand_washing_queryset[idx][believe_in_hand_washing])
        believe_in_hand_washing_data.append(believe_in_hand_washing_queryset[idx]['total'])

    ##########################################################################################################################################

    think_covid_is_gone = 'think_covid_is_gone'
    think_covid_is_gone_queryset= list(Responses.objects.all().values(think_covid_is_gone).annotate(total=Count(think_covid_is_gone)).order_by('total'))

    believe_in_social_distancing_labels=[]
    believe_in_social_distancing_data=[]

    for idx,item in enumerate(think_covid_is_gone_queryset):
        think_covid_is_gone_labels.append(think_covid_is_gone_queryset[idx][think_covid_is_gone])
        think_covid_is_gone_data.append(think_covid_is_gone_queryset[idx]['total'])

    ##########################################################################################################################################

    think_we_need_covid_vaccine = 'think_we_need_covid_vaccine'
    think_we_need_covid_vaccine_queryset= list(Responses.objects.all().values(think_we_need_covid_vaccine).annotate(total=Count(think_we_need_covid_vaccine)).order_by('total'))

    believe_in_social_distancing_labels=[]
    believe_in_social_distancing_data=[]

    for idx,item in enumerate(think_we_need_covid_vaccine_queryset):
        think_covid_is_gone_labels.append(think_we_need_covid_vaccine_queryset[idx][think_we_need_covid_vaccine])
        think_covid_is_gone_data.append(think_we_need_covid_vaccine_queryset[idx]['total'])

    ##########################################################################################################################################
 
    think_vaccines_are_safe = 'think_vaccines_are_safe'
    think_vaccines_are_safe_queryset= list(Responses.objects.all().values(think_vaccines_are_safe).annotate(total=Count(think_vaccines_are_safe)).order_by('total'))

    think_vaccines_are_safe_labels=[]
    think_vaccines_are_safe_data=[]

    for idx,item in enumerate(think_vaccines_are_safe_queryset):
        think_vaccines_are_safe_labels.append(think_vaccines_are_safe_queryset[idx][think_vaccines_are_safe])
        think_vaccines_are_safe_data.append(think_vaccines_are_safe_queryset[idx]['total'])

    ##########################################################################################################################################

    heard_of_any_covid_candidate_vaccine = 'heard_of_any_covid_candidate_vaccine'
    heard_of_any_covid_candidate_vaccine_queryset= list(Responses.objects.all().values(heard_of_any_covid_candidate_vaccine).annotate(total=Count(heard_of_any_covid_candidate_vaccine)).order_by('total'))

    heard_of_any_covid_candidate_vaccine_labels=[]
    heard_of_any_covid_candidate_vaccine_data=[]

    for idx,item in enumerate(heard_of_any_covid_candidate_vaccine_queryset):
        heard_of_any_covid_candidate_vaccine_labels.append(heard_of_any_covid_candidate_vaccine_queryset[idx][heard_of_any_covid_candidate_vaccine])
        heard_of_any_covid_candidate_vaccine_data.append(heard_of_any_covid_candidate_vaccine_queryset[idx]['total'])

    ##########################################################################################################################################

    participate_in_clinical_covid_vaccine_trial = 'participate_in_clinical_covid_vaccine_trial'
    participate_in_clinical_covid_vaccine_trial_queryset= list(Responses.objects.all().values(participate_in_clinical_covid_vaccine_trial).annotate(total=Count(participate_in_clinical_covid_vaccine_trial)).order_by('total'))

    participate_in_clinical_covid_vaccine_trial_labels=[]
    participate_in_clinical_covid_vaccine_trial_data=[]

    for idx,item in enumerate(heard_of_any_covid_candidate_vaccine_queryset):
        participate_in_clinical_covid_vaccine_trial_labels.append(participate_in_clinical_covid_vaccine_trial_queryset[idx][participate_in_clinical_covid_vaccine_trial])
        participate_in_clinical_covid_vaccine_trial_data.append(participate_in_clinical_covid_vaccine_trial_queryset[idx]['total'])

    ##########################################################################################################################################

    reason_not_to_participate_in_clinical_covid_vaccine_trial = 'reason_not_to_participate_in_clinical_covid_vaccine_trial'
    reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset= list(Responses.objects.all().values(reason_not_to_participate_in_clinical_covid_vaccine_trial).annotate(total=Count(reason_not_to_participate_in_clinical_covid_vaccine_trial)).order_by('total'))

    participate_in_clinical_covid_vaccine_trial_labels=[]
    participate_in_clinical_covid_vaccine_trial_data=[]

    for idx,item in enumerate(heard_of_any_covid_candidate_vaccine_queryset):
        reason_not_to_participate_in_clinical_covid_vaccine_trial_labels.append(reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset[idx][participate_in_clinical_covid_vaccine_trial])
        reason_not_to_participate_in_clinical_covid_vaccine_trial_data.append(reason_not_to_participate_in_clinical_covid_vaccine_trial_queryset[idx]['total'])

    ##########################################################################################################################################

    motivation_for_participation = 'motivation_for_participation'
    motivation_for_participation_queryset= list(Responses.objects.all().values(motivation_for_participation).annotate(total=Count(motivation_for_participation)).order_by('total'))

    ##########################################################################################################################################

    route_of_vaccine_administration = 'route_of_vaccine_administration'
    route_of_vaccine_administration_queryset= list(Responses.objects.all().values(route_of_vaccine_administration).annotate(total=Count(route_of_vaccine_administration)).order_by('total'))

    ##########################################################################################################################################

    type_of_vaccine_acceptable = 'type_of_vaccine_acceptable'
    type_of_vaccine_acceptable_queryset= list(Responses.objects.all().values(type_of_vaccine_acceptable).annotate(total=Count(type_of_vaccine_acceptable)).order_by('total'))

    ##########################################################################################################################################

    phase_of_clinical_trial_to_participate_in = 'phase_of_clinical_trial_to_participate_in'
    phase_of_clinical_trial_to_participate_in_queryset= list(Responses.objects.all().values(phase_of_clinical_trial_to_participate_in).annotate(total=Count(phase_of_clinical_trial_to_participate_in)).order_by('total'))

    ##########################################################################################################################################

    country_of_vaccine_influence_your_decision_to_participate = 'country_of_vaccine_influence_your_decision_to_participate'
    country_of_vaccine_influence_your_decision_to_participate_queryset= list(Responses.objects.all().values(country_of_vaccine_influence_your_decision_to_participate).annotate(total=Count(country_of_vaccine_influence_your_decision_to_participate)).order_by('total'))

    ##########################################################################################################################################

    preferred_vaccine_continent = 'preferred_vaccine_continent'
    preferred_vaccine_continent_queryset= list(Responses.objects.all().values(preferred_vaccine_continent).annotate(total=Count(preferred_vaccine_continent)).order_by('total'))

    ##########################################################################################################################################

    vaccine_scientists_should_include_ghanaian = 'vaccine_scientists_should_include_ghanaian'
    vaccine_scientists_should_include_ghanaian_queryset= list(Responses.objects.all().values(vaccine_scientists_should_include_ghanaian).annotate(total=Count(vaccine_scientists_should_include_ghanaian)).order_by('total'))

    ##########################################################################################################################################

    participate_in_mass_covid_vaccination = 'participate_in_mass_covid_vaccination'
    participate_in_mass_covid_vaccination_queryset= list(Responses.objects.all().values(participate_in_mass_covid_vaccination).annotate(total=Count(participate_in_mass_covid_vaccination)).order_by('total'))

    ##########################################################################################################################################

    prepared_to_pay_for_vaccine = 'prepared_to_pay_for_vaccine'
    prepared_to_pay_for_vaccine_queryset= list(Responses.objects.all().values(prepared_to_pay_for_vaccine).annotate(total=Count(prepared_to_pay_for_vaccine)).order_by('total'))

    ##########################################################################################################################################

    estimated_vaccine_cost_range = 'estimated_vaccine_cost_range'
    estimated_vaccine_cost_range_queryset= list(Responses.objects.all().values(estimated_vaccine_cost_range).annotate(total=Count(estimated_vaccine_cost_range)).order_by('total'))

    ##########################################################################################################################################

    origin_of_vaccine_influence_your_decision_to_participate = 'origin_of_vaccine_influence_your_decision_to_participate'
    origin_of_vaccine_influence_your_decision_to_participate_queryset= list(Responses.objects.all().values(origin_of_vaccine_influence_your_decision_to_participate).annotate(total=Count(origin_of_vaccine_influence_your_decision_to_participate)).order_by('total'))

    ##########################################################################################################################################

    preferred_vaccine_origin = 'preferred_vaccine_origin'
    preferred_vaccine_origin_queryset= list(Responses.objects.all().values(preferred_vaccine_origin).annotate(total=Count(preferred_vaccine_origin)).order_by('total'))

    ##########################################################################################################################################


    return render(request, 'user_app/registration/login_success.html', {
    'age_count':age_count, 'marital_status_count':marital_status_count,
    'religion_count':religion_count, 'job_type_count':job_type_count, 'job_category_health_related_count':job_category_health_related_count,
    'clinical_or_nonclinical_job_count':clinical_or_nonclinical_job_count, 'covid_knowledge_before_survey_count':covid_knowledge_before_survey_count,
    'risk_of_covid_exposure_count':risk_of_covid_exposure_count, 'know_of_anyone_diagnosed_with_covid_count':know_of_anyone_diagnosed_with_covid_count,
    'know_of_anyone_hospitalized_due_to_covid_count':know_of_anyone_hospitalized_due_to_covid_count, 'know_of_anyone_die_due_to_covid_count':know_of_anyone_die_due_to_covid_count,
    'know_of_covid_preventive_measures_count':know_of_covid_preventive_measures_count, 'believe_in_facemask_protection_count':believe_in_facemask_protection_count,
    'believe_in_social_distancing_count':believe_in_social_distancing_count, 'believe_in_hand_washing_count':believe_in_hand_washing_count,
    'think_covid_is_gone_count':think_covid_is_gone_count, 'think_we_need_covid_vaccine_count':think_we_need_covid_vaccine_count, 'think_vaccines_are_safe_count':think_vaccines_are_safe_count,
    'heard_of_any_covid_candidate_vaccine_count':heard_of_any_covid_candidate_vaccine_count, 'participate_in_clinical_covid_vaccine_trial_count':participate_in_clinical_covid_vaccine_trial_count,
    'reason_not_to_participate_in_clinical_covid_vaccine_trial_count':reason_not_to_participate_in_clinical_covid_vaccine_trial_count, 'motivation_for_participation_count':motivation_for_participation_count,
    'route_of_vaccine_administration_count':route_of_vaccine_administration_count, 'type_of_vaccine_acceptable_count':type_of_vaccine_acceptable_count,
    'phase_of_clinical_trial_to_participate_in_count':phase_of_clinical_trial_to_participate_in_count, 'country_of_vaccine_influence_your_decision_to_participate_count':country_of_vaccine_influence_your_decision_to_participate_count,
    'preferred_vaccine_continent_count':preferred_vaccine_continent_count, 'vaccine_scientists_should_include_ghanaian_count':vaccine_scientists_should_include_ghanaian_count, 'participate_in_mass_covid_vaccination_count':participate_in_mass_covid_vaccination_count,
    'prepared_to_pay_for_vaccine_count':prepared_to_pay_for_vaccine_count, 'estimated_vaccine_cost_range_count':estimated_vaccine_cost_range_count, 'origin_of_vaccine_influence_your_decision_to_participate_count':origin_of_vaccine_influence_your_decision_to_participate_count,
    'preferred_vaccine_origin_count':preferred_vaccine_origin_count
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


