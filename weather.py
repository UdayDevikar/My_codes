import requests
import json
city=input('enter city')
url=('http://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&appid=7ea32f8e87fc4f3e6b4868da4594479f' % city)
r=requests.get(url)  							# object of type response 
text=r.json()								     # cretaing a object python dictionary 
new=json.dumps(text, indent=10)	# creting a json string for apply indent to easily solve problem 
print(new)									    # printing a json string to easily analyse what output we need 
print(text['name'])				
print(text['sys']['country'])  # applying slicing to get  a required output
print(text['main']['temp'])
