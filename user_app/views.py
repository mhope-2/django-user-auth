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

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    marital_status = 'marital_status'
    marital_status_count = list(Responses.objects.all().values(marital_status).annotate(total=Count(marital_status)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    religion = 'religion'
    religion_count = list(Responses.objects.all().values(religion).annotate(total=Count(religion)).order_by('total'))

    job_type = 'job_type'
    job_type_count = list(Responses.objects.all().values(job_type).annotate(total=Count(job_type)).order_by('total'))

    job_category_health_related = 'job_category_health_related'
    job_category_health_related_count = list(Responses.objects.all().values(job_category_health_related).annotate(total=Count(job_category_health_related)).order_by('total'))

    clinical_or_nonclinical_job = 'clinical_or_nonclinical_job'
    clinical_or_nonclinical_job_count = list(Responses.objects.all().values(clinical_or_nonclinical_job).annotate(total=Count(clinical_or_nonclinical_job)).order_by('total'))

    covid_knowledge_before_survey = 'covid_knowledge_before_survey'
    covid_knowledge_before_survey_count = list(Responses.objects.all().values(covid_knowledge_before_survey).annotate(total=Count(covid_knowledge_before_survey)).order_by('total'))

    risk_of_covid_exposure = 'risk_of_covid_exposure'
    risk_of_covid_exposure = list(Responses.objects.all().values(risk_of_covid_exposure).annotate(total=Count(risk_of_covid_exposure)).order_by('total'))

    know_of_anyone_diagnosed_with_covid = 'know_of_anyone_diagnosed_with_covid'
    know_of_anyone_diagnosed_with_covid_count = list(Responses.objects.all().values(know_of_anyone_diagnosed_with_covid).annotate(total=Count(know_of_anyone_diagnosed_with_covid)).order_by('total'))

    know_of_anyone_hospitalized_due_to_covid = 'know_of_anyone_hospitalized_due_to_covid'
    know_of_anyone_hospitalized_due_to_covid_count = list(Responses.objects.all().values(know_of_anyone_hospitalized_due_to_covid).annotate(total=Count(know_of_anyone_hospitalized_due_to_covid)).order_by('total'))

    know_of_anyone_die_due_to_covid = 'know_of_anyone_die_due_to_covid'
    know_of_anyone_die_due_to_covid_count = list(Responses.objects.all().values(know_of_anyone_die_due_to_covid).annotate(total=Count(know_of_anyone_die_due_to_covid)).order_by('total'))

    know_of_covid_preventive_measures = 'know_of_covid_preventive_measures'
    know_of_covid_preventive_measures_count = list(Responses.objects.all().values(know_of_covid_preventive_measures).annotate(total=Count(know_of_covid_preventive_measures)).order_by('total'))

    believe_in_facemask_protection = 'believe_in_facemask_protection'
    believe_in_facemask_protection_count = list(Responses.objects.all().values(believe_in_facemask_protection).annotate(total=Count(believe_in_facemask_protection)).order_by('total'))

    believe_in_social_distancing = 'believe_in_social_distancing'
    believe_in_social_distancing_count = list(Responses.objects.all().values(believe_in_social_distancing).annotate(total=Count(believe_in_social_distancing)).order_by('total'))

    belive_in_hand_washing = 'belive_in_hand_washing'
    belive_in_hand_washing_count = list(Responses.objects.all().values(belive_in_hand_washing).annotate(total=Count(belive_in_hand_washing)).order_by('total'))

    think_covid_is_gone = 'think_covid_is_gone'
    think_covid_is_gone_count = list(Responses.objects.all().values(think_covid_is_gone).annotate(total=Count(think_covid_is_gone)).order_by('total'))

    think_we_need_covid_vaccine = 'think_we_need_covid_vaccine'
    think_we_need_covid_vaccine_count = list(Responses.objects.all().values(think_we_need_covid_vaccine).annotate(total=Count(think_we_need_covid_vaccine)).order_by('total'))

    think_vaccines_are_safe = 'think_vaccines_are_safe'
    think_vaccines_are_safe_count = list(Responses.objects.all().values(think_vaccines_are_safe).annotate(total=Count(think_vaccines_are_safe)).order_by('total'))

    heard_of_any_covid_candidate_vaccine = 'heard_of_any_covid_candidate_vaccine'
    heard_of_any_covid_candidate_vaccine_count = list(Responses.objects.all().values(heard_of_any_covid_candidate_vaccine).annotate(total=Count(heard_of_any_covid_candidate_vaccine)).order_by('total'))

    participate_in_clinical_covid_vaccine_trial = 'participate_in_clinical_covid_vaccine_trial'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    participate_in_clinical_covid_vaccine_trial = 'participate_in_clinical_covid_vaccine_trial'
    participate_in_clinical_covid_vaccine_trial = list(Responses.objects.all().values(participate_in_clinical_covid_vaccine_trial).annotate(total=Count(participate_in_clinical_covid_vaccine_trial)).order_by('total'))

    reason_not_to_participate_in_clinical_covid_vaccine_trial = 'reason_not_to_participate_in_clinical_covid_vaccine_trial'
    reason_not_to_participate_in_clinical_covid_vaccine_trial_count = list(Responses.objects.all().values(reason_not_to_participate_in_clinical_covid_vaccine_trial).annotate(total=Count(reason_not_to_participate_in_clinical_covid_vaccine_trial)).order_by('total'))

    motivation_for_participation = 'motivation_for_participation'
    motivation_for_participation_count = list(Responses.objects.all().values(motivation_for_participation).annotate(total=Count(motivation_for_participation)).order_by('total'))

    route_of_vaccine_administration = 'route_of_vaccine_administration'
    route_of_vaccine_administration_count = list(Responses.objects.all().values(route_of_vaccine_administration).annotate(total=Count(route_of_vaccine_administration)).order_by('total'))

    type_of_vaccine_acceptable = 'type_of_vaccine_acceptable'
    type_of_vaccine_acceptable_count = list(Responses.objects.all().values(type_of_vaccine_acceptable).annotate(total=Count(type_of_vaccine_acceptable)).order_by('total'))

    phase_of_clinical_trial_to_participate_in = 'phase_of_clinical_trial_to_participate_in'
    phase_of_clinical_trial_to_participate_in_count = list(Responses.objects.all().values(phase_of_clinical_trial_to_participate_in).annotate(total=Count(phase_of_clinical_trial_to_participate_in)).order_by('total'))

    country_of_vaccine_influence_your_decision_to_participate = 'country_of_vaccine_influence_your_decision_to_participate'
    country_of_vaccine_influence_your_decision_to_participate_count = list(Responses.objects.all().values(country_of_vaccine_influence_your_decision_to_participate).annotate(total=Count(country_of_vaccine_influence_your_decision_to_participate)).order_by('total'))

    preferred_vaccine_continent = 'preferred_vaccine_continent'
    preferred_vaccine_continent_count = list(Responses.objects.all().values(preferred_vaccine_continent).annotate(total=Count(preferred_vaccine_continent)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))

    age = 'age'
    age_count = list(Responses.objects.all().values(age).annotate(total=Count(age)).order_by('total'))

    gender = 'gender'
    gender_count = list(Responses.objects.all().values(gender).annotate(total=Count(gender)).order_by('total'))






    return render(request, 'user_app/registration/login_success.html', 
                                                {'age_count':age_count})


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.is_active = True
    user.save()

    return redirect('user_login')


