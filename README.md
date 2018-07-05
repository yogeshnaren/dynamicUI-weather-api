# Weather Data - Dynamic UI using DJANGO REST Framework
_Dynamic UI RESTful API for Weather Information for Six Days including the given date using Python Django Rest Framework._

_Current forecast is retreived from Yahoo Weather API._

### AIM:
Creating a Dynamic UI using jQuery and Javascript with REST Framework in Django that provides data of weather and current forecast weather information for given dat using Yahoo Weather.

### WORKING:

Dynamic UI is rendered using jQuery and Javascript 
RESTful Web services is deployed using swagger to host Weather Information and forecast. Following endpoints are created to perform

#### 1.	Weather Information (for Six days):

_Methods:_

##### GET 
Displays weather information for six dates with the date specified and maximum and minimum temperatures in high and low sections. 

### TECHNOLOGIES USED:

* Programming language : Python
* Framework :  		Django Rest Framework
* WebAPI : 			Swagger
* DB     : 			SQLite (Django Internal)
* Dynamic UI : Javascript, jQuery

A database is created in which a table accepts a .csv file to insert data into it.

### PARAMETERS (INPUT & OUTPUT):

* DATE: String
* TMIN:  Integer
* TMAX: Integer

##### Accepted Input URLs: 
* http://18.218.214.7:8000/


##### Forecast Data
It returns the Date, High and Low for 6 days including the date provided in the Datepicker.

### RESOURCES :

* http://www.django-rest-framework.org/
* https://django-rest-swagger.readthedocs.io/en/latest/

### LINKS:
* "app_url"  :   	"http://18.218.214.7:8000/", 
* "code_url": 	"https://github.uc.edu/bundeyyn/dynamicUI-weather-forecast", 
* "doc_url"  : 	"https://github.uc.edu/bundeyyn/dynamicUI-weather-forecast/blob/master/README.md"
