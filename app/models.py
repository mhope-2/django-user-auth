from django.db import models
from django.utils import timezone

# Create your models here.
class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=12)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = "phone"
        verbose_name_plural = "phones"

class OTP(models.Model):
    id = models.IntegerField(primary_key=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.otp)

    class Meta:
        verbose_name = "otp"
        verbose_name_plural = "otps"


class Responses(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    religion_other = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=255, blank=True, null=True)
    job_type_other = models.CharField(max_length=255, blank=True, null=True)
    job_category_health_related = models.CharField(max_length=255, blank=True, null=True)
    clinical_or_nonclinical_job = models.CharField(max_length=255, blank=True, null=True)
    covid_knowledge_before_survey = models.CharField(max_length=255, blank=True, null=True)
    risk_of_covid_exposure = models.CharField(max_length=255, blank=True, null=True)
    know_of_anyone_diagnosed_with_covid = models.CharField(max_length=255, blank=True, null=True)
    know_of_anyone_hospitalized_due_to_covid = models.CharField(max_length=255, blank=True, null=True)
    know_of_anyone_die_due_to_covid = models.CharField(max_length=255, blank=True, null=True)
    know_of_covid_preventive_measures = models.CharField(max_length=255, blank=True, null=True)
    believe_in_facemask_protection = models.CharField(max_length=255, blank=True, null=True)
    believe_in_social_distancing = models.CharField(max_length=255, blank=True, null=True)
    belive_in_hand_washing = models.CharField(max_length=255, blank=True, null=True)
    think_covid_is_gone = models.CharField(max_length=255, blank=True, null=True)
    think_we_need_covid_vaccine = models.CharField(max_length=255, blank=True, null=True)
    think_vaccines_are_safe = models.CharField(max_length=255, blank=True, null=True)
    heard_of_any_covid_candidate_vaccine = models.CharField(max_length=255, blank=True, null=True)
    participate_in_clinical_covid_vaccine_trial = models.CharField(max_length=255, blank=True, null=True)
    reason_not_to_participate_in_clinical_covid_vaccine_trial = models.CharField(max_length=255, blank=True, null=True)
    reason_not_to_participate_in_clinical_covid_vaccine_trial_other = models.CharField(max_length=255, blank=True, null=True)
    motivation_for_participation = models.CharField(max_length=255, blank=True, null=True)
    route_of_vaccine_administration = models.CharField(max_length=255, blank=True, null=True)
    type_of_vaccine_acceptable = models.CharField(max_length=255, blank=True, null=True)
    phase_of_clinical_trial_to_participate_in = models.CharField(max_length=255, blank=True, null=True)
    country_of_vaccine_influence_your_decision_to_participate = models.CharField(max_length=255, blank=True, null=True)
    preferred_vaccine_continent = models.CharField(max_length=255, blank=True, null=True)
    vaccine_scientists_should_include_ghanaian = models.CharField(max_length=255, blank=True, null=True)
    participate_in_mass_covid_vaccination = models.CharField(max_length=255, blank=True, null=True)
    prepared_to_pay_for_vaccine = models.CharField(max_length=255, blank=True, null=True)
    estimated_vaccine_cost_range = models.CharField(max_length=255, blank=True, null=True)
    origin_of_vaccine_influence_your_decision_to_participate = models.CharField(max_length=255, blank=True, null=True)
    preferred_vaccine_origin = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField('Created Date', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = "responses"
        verbose_name_plural = "responses"

