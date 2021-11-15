import json
#request,urllib3, httplib3 ...
#pip install requests

import requests
#this url is to connect to api data and can come from api 
#open weather map is a real time weather data from (nasa satellitle). Lot of websites or other sources use this website api to get the real time data
#It is built in django framework , python language

url="http://api.openweathermap.org/data/2.5/weather?q=chennai&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73"
response= requests.get(url)
print(response.headers)
print(f"Content type{response.headers['Content-Type']}")
report =json.loads(response.text)
print(type(report)) # class dict
print(report)

desc =report['weather'][0]['description']
print("status :",desc)
