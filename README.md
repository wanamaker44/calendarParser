# calendarParser
Parses text file from Brookline softball schedule email into a file that can be uploaded into google calendar.


## future plans
In the future it would be great to build this into a flask app that could be fronted by a simple web UI where the user could simply copy and paste in text from an email and then directly upload it to their connected Google Calendar.


## architecture
### flask microservice
The microservice hosts the static html/js/css content and the convertData function. 

### static files
The static files display a text area for entering in the unparsed calendar content. The user submits the content through this form and it gets POSTed to the flask microservice. Upon parsing the content, the microservice then sends back a parsed csv file.