import json
import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
ottawa_wards_response_json = ottawa_wards_response.json()

for item in ottawa_wards_response_json['objects']:
    print(item['name'])
