import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={"dak_dagorik_type" : 1,"from_office_id" :65,"from_office_unit_id" :5121,"from_officer_id" : 77858,"from_officer_designation_id" : 12643, "to_office_id" : 65,"to_office_unit_id" : 5121,"to_officer_id" : 77847,"to_officer_designation_id" : 12642, "attention_type" : 1,"operation_type" : 1, "dak_priority": 0})
print(r.json())



