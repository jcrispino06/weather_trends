import requests
import sys

import json

response = requests.request("GET",
                            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/953%20Danby%20Rd%2C%20Ithaca%2C%20NY%2014850?unitGroup=us&key=G2R4G25J2SRE2HDPBB7MP4MFR&contentType=json")
if response.status_code != 200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()

# Parse the results as JSON
jsonData = json.dumps(response.json())
data = json.loads(jsonData)
print(f"Weather for {data['days'][0]['datetime']}")
print(f"Max temp: {data['days'][0]['tempmax']}F")
print(f"Current temp: {data['days'][0]['temp']}F")
print(f"Min temp: {data['days'][0]['tempmin']}F")