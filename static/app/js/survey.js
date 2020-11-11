window.onload = function () {
  //   window.location.reload();

  document.body.onload = function() {
  window.extents.postMessage(document.body.offsetHeight)
}

  var dispatcher = new cf.EventDispatcher();
  dispatcher.addEventListener(
    cf.FlowEvents.USER_INPUT_UPDATE,
    function (event) {
      // console.log(event)
      var userInput = event.detail.text;
      var formDataSerialized = conversationalForm.getFormData(true);

      if (userInput === "Hello" || userInput === "Hi") {
        conversationalForm.addRobotChatResponse("Hello 😊");
      }
    },
    false
  );

  const conversationalForm = new window.cf.ConversationalForm.startTheConversation(
    {
      formEl: document.getElementById("form"),
      context: document.getElementById("cf-context"),
      robotImage: "/static/app/assets/imgs/maame.png",
      userImage: "/static/app/assets/imgs/user.png",
      eventDispatcher: dispatcher,
      loadExternalStyleSheet: true,
      submitCallback: function () {
        // conversationalForm.addRobotChatResponse("Survey Complete. Your response has been submitted. Thank you for your time. 😊"); 
        const formDataSerialized = conversationalForm.getFormData(true);
        console.log(formDataSerialized);
        console.log()

        //JSONIFY
        let jsonString = {
          age: String(formDataSerialized["cfc-q1"]),
          gender: String(formDataSerialized["cfc-q2"][0]),
          marital_status: String(formDataSerialized["cfc-q3"][0]),
          religion: String(formDataSerialized["cfc-q4"][0]),
          religion_other: String(formDataSerialized["cfc-q4-other"]),
          job_type: String(formDataSerialized["cfc-q5"][0]),
          job_type_other: String(formDataSerialized["cfc-q5-other"]),
          nationality: String(formDataSerialized["cfc-q6"]),
          country: String(formDataSerialized["cfc-q7"]),
          job_category_health_related: String(formDataSerialized["cfc-q8"][0]),
          clinical_or_nonclinical_job: String(formDataSerialized["cfc-q9"][0]),
          covid_knowledge: String(formDataSerialized["cfc-q10"][0]),
          exposed_to_covid: String(formDataSerialized["cfc-q11"][0]),
          know_of_anyone_diagnosed_with_covid: String(formDataSerialized["cfc-q12"][0]),
          know_of_anyone_hospitalized_due_to_covid: String(formDataSerialized["cfc-q13"][0]),
          know_of_anyone_die_due_to_covid: String(formDataSerialized["cfc-q14"][0]),
          know_of_covid_preventive_measures: String(formDataSerialized["cfc-q15"][0]),
          believe_in_facemask_protection: String(formDataSerialized["cfc-q16"][0]),
          believe_in_social_distancing: String(formDataSerialized["cfc-q17"][0]),
          belive_in_hand_washing: String(formDataSerialized["cfc-q18"][0]),
          think_covid_is_gone: String(formDataSerialized["cfc-q19"][0]),
          think_we_need_covid_vaccine: String(formDataSerialized["cfc-q20"][0]),
          think_vaccines_are_safe: String(formDataSerialized["cfc-q21"][0]),
          heard_of_any_covid_candidate_vaccine: String(formDataSerialized["cfc-q22"][0]),
          participate_in_clinical_covid_vaccine_trial: String(formDataSerialized["cfc-q23"][0]),
          reason_not_to_participate_in_clinical_covid_vaccine_trial: String(formDataSerialized["cfc-q24"][0]),
          reason_not_to_participate_in_clinical_covid_vaccine_trial_other: String(formDataSerialized["cfc-24-other"]),
          motivation_for_participation: String(formDataSerialized["cfc-q25"][0]),
          route_of_vaccine_administration: String(formDataSerialized["cfc-q26"][0]),
          type_of_vaccine_acceptable: String(formDataSerialized["cfc-q27"][0]),
          phase_of_clinical_trial_to_participate_in: String(formDataSerialized["cfc-q28"][0]),
          country_of_vaccine_influence_your_decision_to_participate: String(formDataSerialized["cfc-q29"][0]),
          preferred_vaccine_continent: String(formDataSerialized["cfc-q30"][0]),
          vaccine_scientists_should_include_ghanaian: String(formDataSerialized["cfc-q31"][0]),
          participate_in_mass_covid_vaccination: String(formDataSerialized["cfc-q32"][0]),
          prepared_to_pay_for_vaccine: String(formDataSerialized["cfc-q33"][0]),
          vaccine_cost_range: String(formDataSerialized["cfc-q34"][0]),
          origin_of_vaccine_influence_your_decision_to_participate: String(formDataSerialized["cfc-q35"][0]),
          preferred_vaccine_origin: String(formDataSerialized["cfc-q36"][0])
        };

        console.log("JSONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\n",jsonString);

        // GENERATE OTP
        // var random_number = Math.floor(100000 + Math.random() * 900000);
        // console.log(random_number)

        
        // get_url="http://localhost:5000"
        let headers = new Headers();

        headers.append("Content-Type", "application/json");
        headers.append("Accept", "application/json");

        headers.append(
          "Access-Control-Allow-Origin",
          "https://cors-anywhere.herokuapp.com/https://api.sumitomo.snwolley.com/data"
        );
        headers.append("Access-Control-Allow-Credentials", "true");



    //  console.log(JSON.stringify(jsonString))
        //push form data to db
      // $.ajax({
      //   method: "POST",
      //   headers: headers,
      //   url:
      //     "https://cors-anywhere.herokuapp.com/https://api.sumitomo.snwolley.com/data",
      //   crossDomain: true,
      //   contentType: "application/json",
      //   data: JSON.stringify(jsonString),
      //   dataType: "json",
      //   success: function (data) {
      //     console.log(data);
      //   },
      //   error: function (err) {
      //     console.log("ERROR: ",err);
      //   },
      // });





      
        conversationalForm.remapTagsAndStartFrom(1, 1, true);
      },
    }
  );
};
