import requests
import json
import time
import csv

API_URL = "http://ece444lab5-env.eba-p7jqbfmb.us-east-1.elasticbeanstalk.com/predict"

test_cases = {
    "fake_1": "Breaking news: Scientists confirm Earth is flat and NASA hid the truth!",
    "fake_2": "Government secretely replaces the moon with a hologram to hide alien base.",
    "real_1": "Antidepressants can cause significant weight changes, health impacts even after just a few weeks, research shows.",
    "real_2": "Staff shortages shutting two Canadian airport control towers periodically, memo says"
}

try:
    csvfile = open('data.csv', 'w', newline='')
    with csvfile as f:
        f.truncate(0) 
        writer = csv.writer(f)
        writer.writerow(['test_case', 'call_number', 'latency_seconds'])
        
        for label, text in test_cases.items():
            for i in range(100):
                start = time.time()
                response = requests.post(API_URL, json={"text": text})
                end = time.time()
                latency = end - start
                writer.writerow([label, i+1, latency])
            print("done")
finally:
    csvfile.close()
    print("Completed all test cases")

            