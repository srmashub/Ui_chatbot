from rasa_core.actions import Action
from rasa_core.events import Restarted
from rasa_core.actions.forms import (
    BooleanFormField,
    EntityFormField,
    FormAction,
    FreeTextFormField
)
from rasa_core_sdk.events import SlotSet
import httplib2
import requests


class ActionappIssue(FormAction):

	RANDOMIZE=False
	
	@staticmethod
	def required_fields():
		return[
		EntityFormField("application", "application"),
		EntityFormField("description", "description")
		]
		
	def name(self):
		return "action_application"
		
	def submit(self,dispatcher,tracker,domain):
		s=str(tracker.get_slot("application"))
		url="https://www."+s+".com"
		
		return[]
		
class ActionurlIssue(FormAction):

	RANDOMIZE=False
	
	@staticmethod
	def required_fields():
		return[
		EntityFormField("url", "url"),
		EntityFormField("description", "description")
		]
		
	def name(self):
		return "action_url"
		
	def submit(self,dispatcher,tracker,domain):
		s=str(tracker.get_slot("url"))
		url="https://www."+s+".com"
		
		return[]
		
class ActionopenApplication(FormAction):

	RANDOMIZE=False
	
	@staticmethod
	def required_fields():
		return[
		EntityFormField("application", "application")
		]
		
	def name(self):
		return "action_openapplication"
		
	def submit(self,dispatcher,tracker,domain):
		s=str(tracker.get_slot("application"))
		url="https://www."+s+".com"
		dispatcher.utter_message("Try this url"+ url)
		return[]
				