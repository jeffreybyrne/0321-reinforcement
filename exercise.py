
import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
ottawa_wards_response_json = ottawa_wards_response.json()

print("Ottawa Wards:")
for item in ottawa_wards_response_json['objects']:
    print(item['name'])

print("======")

rep_set_response = requests.get('https://represent.opennorth.ca/representative-sets/')
rep_set_response_json = rep_set_response.json()

print("Representative Sets:")
for item in rep_set_response_json['objects']:
    print(item['name'])
