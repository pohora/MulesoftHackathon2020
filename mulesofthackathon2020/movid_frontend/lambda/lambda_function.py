# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import requests
import json

import us_state_abbrev

# Use request utils
from ask_sdk_core.utils import get_supported_interfaces
from ask_sdk_model.interfaces.alexa.presentation.apl import (
    RenderDocumentDirective)


#from utils import us_state_abbrev    


# APL Document file paths for use in handlers
launchTemplatePath = "launch.json"
launchDataPath="launchData.json"
# Tokens used when sending the APL directives
HELLO_WORLD_TOKEN = "helloworldToken"

def _load_apl_document(file_path):
    # type: (str) -> Dict[str, Any]
    """Load the apl json document at the path into a dict object."""
    with open(file_path) as f:
        return json.load(f)

def supports_apl(handler_input):
    """
    Checks whether APL is supported by the User's device
    """
    supported_interfaces = get_supported_interfaces(
        handler_input)
    return supported_interfaces.alexa_presentation_apl != None        


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can run a Covid Symptom check, check covid information for a state or what current restrictions are in place for a state. Which would you like to try?"
        
        
        #if supports_apl(handler_input) is not None:
        if get_supported_interfaces(handler_input).alexa_presentation_apl is not None:
            return(
                handler_input.response_builder.speak(speak_output).add_directive(
                RenderDocumentDirective(
                   token="pagerToken",
                   document=_load_apl_document("./templates/launch.json"),
                   datasources=_load_apl_document("./data/launchData.json")
                )
             )
             .ask(speak_output)
             .response
             )
        else:
            return(
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
            )
            
        


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class SymptomCheckerIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SymptomCheckerIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        # Get any existing attributes from the incoming request
        session_attr = handler_input.attributes_manager.session_attributes
        
        speak_output = "Finding recommendation now."
        slots = handler_input.request_envelope.request.intent.slots
        age = slots['age']
        if age.value:
            session_attr["age"]=age.value
            speak_output=speak_output+age.value
        else:
            speak_output=speak_output+" no age value provided. "
        gender=slots['gender']    
        if gender.value:
            session_attr["gender"]=gender.value
            speak_output=speak_output+gender.value
        else:
            speak_output=speak_output+" no gender value provided. "
        lifeThreateningSymptoms=slots['lifeThreateningSymptoms']    
        if lifeThreateningSymptoms.value:
            session_attr["lifeThreateningSymptoms"]=lifeThreateningSymptoms.value
            speak_output=speak_output+lifeThreateningSymptoms.value
        else:
            speak_output=speak_output+" no lifeThreateningSymptoms value provided. "
        hasSymptoms=slots['hasSymptoms']    
        if hasSymptoms.value:
            session_attr["hasSymptoms"]=hasSymptoms.value
            speak_output=speak_output+hasSymptoms.value
        else:
            speak_output=speak_output+" no hasSymptoms value provided. "
        feelingSick=slots['feelingSick']    
        if feelingSick.value:
            session_attr["feelingSick"]=feelingSick.value
            speak_output=speak_output+feelingSick.value
        else:
            speak_output=speak_output+" no feelingSick value provided. "
        liveInLongTermCareFacility=slots['liveInLongTermCareFacility']    
        if liveInLongTermCareFacility.value:
            session_attr["liveInLongTermCareFacility"]=liveInLongTermCareFacility.value
            speak_output=speak_output+liveInLongTermCareFacility.value
        else:
            speak_output=speak_output+" no liveInLongTermCareFacility value provided. "
        lastTwoWeeksHealthCareFacility=slots['lastTwoWeeksHealthCareFacility']    
        if lastTwoWeeksHealthCareFacility.value:
            session_attr["lastTwoWeeksHealthCareFacility"]=lastTwoWeeksHealthCareFacility.value
            speak_output=speak_output+lastTwoWeeksHealthCareFacility.value
        else:
            speak_output=speak_output+" no lastTwoWeeksHealthCareFacility value provided. "
        hasChronicCondition=slots['hasChronicCondition']    
        if hasChronicCondition.value:
            session_attr["hasChronicCondition"]=hasChronicCondition.value
            speak_output=speak_output+hasChronicCondition.value
        else:
            speak_output=speak_output+" no hasChronicCondition value provided. "
        lastTwoWeeksPresenceCovidInfected=slots['lastTwoWeeksPresenceCovidInfected']    
        if lastTwoWeeksPresenceCovidInfected.value:
            session_attr["lastTwoWeeksPresenceCovidInfected"]=lastTwoWeeksPresenceCovidInfected.value
            speak_output=speak_output+lastTwoWeeksPresenceCovidInfected.value
        else:
            speak_output=speak_output+" no lastTwoWeeksPresenceCovidInfected value provided. "    
            
        payload = {'age': age.value, 'gender': gender.value,'lifeThreateningSymptoms':lifeThreateningSymptoms.value,'hasSymptoms':hasSymptoms.value,'feelingSick':feelingSick.value,'liveInLongTermCareFacility':liveInLongTermCareFacility.value,'lastTwoWeeksHealthCareFacility':lastTwoWeeksHealthCareFacility.value,'hasChronicCondition':hasChronicCondition.value,'lastTwoWeeksPresenceCovidInfected':lastTwoWeeksPresenceCovidInfected.value}    
        
        response = requests.get("https://movid.us-e2.cloudhub.io/api/symptomchecker/",params=payload)
        
        data=response.json()
        
        #person1=data["people"][0]["name"]
        #speak_output="I received, your "+data['age']+"is and you are "+data['gender'] #speak_output+person1
        speak_output=data["output"]
        
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Would you like to log symptoms?")
                .response
        )        
class ReportSymptomsIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ReportSymptomsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        # Get any existing attributes from the incoming request
        session_attr = handler_input.attributes_manager.session_attributes
        speak_output="Hello"
        
        #We can only send symptoms if we have already captured them in the SymptomCheckerIntent.
        if "lifeThreateningSymptoms" in session_attr:
            #speak_output="Im about to send symptoms. Please hold the line. "
            symptomReport="hasSymptoms: "+session_attr['hasSymptoms']+" feelingSick:"+session_attr['feelingSick']+" lastTwoWeeksPresenceCovidInfected: "+session_attr['lastTwoWeeksPresenceCovidInfected']
            payload={'description':symptomReport}
            response = requests.get("https://movid.us-e2.cloudhub.io/api/logsymptoms/",params=payload)
            data=response.json()
            speak_output = data['message']
            
        else:    
            speak_output = "No data. Please run symptom checker."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Would you like to check Covid information for a state?")
                .response
        )
class StateRestrictionsCheckIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StateRestrictionsCheckIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = "Hello World!"
        state = ask_utils.request_util.get_slot(handler_input, "state")
        if state.value:
            stateName=state.value
        else:
            stateName="unknown"
            
            
        speak_output="Checking current Covid restrictions for "+stateName    
        payload = {'country':'USA','stateCode': us_state_abbrev.us_state_abbrev[stateName]} 
        #https://localcoviddata.com/covid19/v1/high-level-policy?country=USA&state=IN
        response=requests.get("https://movid.us-e2.cloudhub.io/api/stateRestrictions",params=payload)
        
        data=response.json()
        
        speak_output=data['message']
        
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("How can I help?")
                .response
        ) 
        
    
class StateCovidInformationIntentHandler(AbstractRequestHandler):
    """Handler for StateCovidInformationIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StateCovidInformationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        state = ask_utils.request_util.get_slot(handler_input, "state")
        if state.value:
            stateName=state.value
        else:
            stateName="unknown"
            
        payload = {'stateCode': us_state_abbrev.us_state_abbrev[stateName]} 
        #https://localcoviddata.com/covid19/v1/high-level-policy?country=USA&state=IN
        #https://api.covidactnow.org/v2/state/AK.json?apiKey=69709bb8743c4a3ea61819fda5acdd53
        url="https://movid.us-e2.cloudhub.io/api/stateinformation"
        response=requests.get(url,params=payload)
        
        data=response.json()    
            
        speak_output = data['message']

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        ) 
    
    
class StateInfectionRateIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StateInfectionRateIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        state = ask_utils.request_util.get_slot(handler_input, "state")
        if state.value:
            stateName=state.value
        else:
            stateName="unknown"
            
        payload = {'stateCode': us_state_abbrev.us_state_abbrev[stateName]} 
        
        url="https://movid.us-e2.cloudhub.io/api/stateinfectionrate"
        response=requests.get(url,params=payload)
        
        data=response.json()    
            
        speak_output = data['message']

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class StateRiskLevelIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StateRiskLevelsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        state = ask_utils.request_util.get_slot(handler_input, "state")
        if state.value:
            stateName=state.value
        else:
            stateName="unknown"
            
        payload = {'stateCode': us_state_abbrev.us_state_abbrev[stateName]} 
        
        url="https://movid.us-e2.cloudhub.io/api/staterisklevels"
        response=requests.get(url,params=payload)
        
        data=response.json()    
            
        speak_output = data['message']

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )        
    

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(StateRestrictionsCheckIntentHandler())
sb.add_request_handler(SymptomCheckerIntentHandler())
sb.add_request_handler(ReportSymptomsIntentHandler())
sb.add_request_handler(StateCovidInformationIntentHandler())
sb.add_request_handler(StateInfectionRateIntentHandler())
sb.add_request_handler(StateRiskLevelIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()