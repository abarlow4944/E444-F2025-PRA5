### functional/unit tests
import requests
import json

API_URL = "http://ece444lab5-env.eba-p7jqbfmb.us-east-1.elasticbeanstalk.com/predict"

test_cases = {
    "fake_1": "Breaking news: Scientists confirm Earth is flat and NASA hid the truth!",
    "fake_2": "Government secretely replaces the moon with a hologram to hide alien base.",
    "real_1": "Antidepressants can cause significant weight changes, health impacts even after just a few weeks, research shows.",
    "real_2": "Staff shortages shutting two Canadian airport control towers periodically, memo says"
}

for label, text in test_cases.items():
    response = requests.post(API_URL, json={"text": text})
    print(label, "=>", response.json())