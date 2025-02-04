import json
import requests

#API to fecth temp of a city

city_name = input("Enter your city: ")
api_key='bb4956b47038486784eb0193e3c7eeab'  #like passwords

api_url =f'https://api.'your website'.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'  #We are going this url but with a specific city

get_server_info = requests.get(api_url)
data = get_server_info.json()
print(data)

pd= json.dumps(data, indent=4)
print(pd)
