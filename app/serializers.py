from rest_framework import serializers
from app.models import Responses

class ResponseSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    marital_status = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    religion = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    religion_other = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    job_type = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    job_type_other = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    job_category_health_related = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    clinical_or_nonclinical_job = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    covid_knowledge_before_survey = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    risk_of_covid_exposure = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    know_of_anyone_diagnosed_with_covid = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    know_of_anyone_hospitalized_due_to_covid = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    know_of_anyone_die_due_to_covid = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    know_of_covid_preventive_measures = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    believe_in_facemask_protection = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    believe_in_social_distancing = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    belive_in_hand_washing = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    think_covid_is_gone = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    think_we_need_covid_vaccine = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    think_vaccines_are_safe = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    heard_of_any_covid_candidate_vaccine = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    participate_in_clinical_covid_vaccine_trial = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    reason_not_to_participate_in_clinical_covid_vaccine_trial = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    reason_not_to_participate_in_clinical_covid_vaccine_trial_other = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    motivation_for_participation = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    route_of_vaccine_administration = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    type_of_vaccine_acceptable = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    phase_of_clinical_trial_to_participate_in = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    country_of_vaccine_influence_your_decision_to_participate = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    preferred_vaccine_continent = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    vaccine_scientists_should_include_ghanaian = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    participate_in_mass_covid_vaccination = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    prepared_to_pay_for_vaccine = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    estimated_vaccine_cost_range = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    origin_of_vaccine_influence_your_decision_to_participate = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    preferred_vaccine_origin = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)

    class Meta:     #instead of meta write Meta (Capital M)
        model = Responses
        fields = '__all__'