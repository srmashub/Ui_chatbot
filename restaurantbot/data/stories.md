## greet
* greet
    - utter_greet

## thank
* thank
    - utter_thank

## bye
* bye
    - utter_goodbye
	
## App not working
* greet
    - utter_greet
* app_issue
	- action_application
	- slot{"requested_slot": "application"}
* inform{"application": "google"}
	- action_application
	- slot{"requested_slot": "description"}
* inform{"description": "internet issue"}
	- utter_solution
* accept
    - utter_thank
* thank
    - utter_thank
* bye
    - utter_goodbye

## App not working1
* greet
    - utter_greet
* app_issue
	- action_application
	- slot{"requested_slot": "application"}
* inform{"application": "google"}
	- action_application
	- slot{"requested_slot": "description"}
* inform{"description": "internet issue"}
	- utter_solution
* deny
	- utter_deny
	
* thank
    - utter_thank
* bye
    - utter_goodbye




## Url not working
* greet
    - utter_greet
* url_issue
	- action_url
	- slot{"requested_slot": "url"}
* inform{"url": "www.google.com"}
	- action_url
	- slot{"requested_slot": "description"}
* inform{"description": "internet issue"}
	- slot{"description": "internet issue"}
	- utter_solution
* accept
    - utter_thank
* bye
    - utter_goodbye

## Url not working1
* greet
    - utter_greet
* url_issue
	- action_url
	- slot{"requested_slot": "url"}
* inform{"url": "www.google.com"}
	- action_url
	- slot{"requested_slot": "description"}
* inform{"description": "internet issue"}
	- slot{"description": "internet issue"}
	- utter_solution
* deny
	- utter_deny
* bye
    - utter_goodbye
	

## Open Application
* greet
		- utter_greet
* open_application
			- action_openapplication
			- slot{"requested_slot": "application"}
* inform{"application": "google"}
			- action_openapplication
			

			
	
	
	
	
	
