#!/usr/bin/python3

import requests
import json

apiheaders = {'Content-Type': 'application/json', 'Authorization-Token': 'INSERT YOUR API TOKEN HERE'}

kiosk_url = 'https://rock.example.com/api/Devices?$filter=IPAddress ne null and DeviceTypeValueId eq 41'

checkintoken = 'YOUR CHECKIN TOKEN HERE'

getkiosks = requests.get(kiosk_url, headers=apiheaders)

parsed = json.loads(getkiosks.text)

for i in parsed:
    print(i["Name"] + "\n" + "https://rock.example.com/checkin?Kioskid=" + str(i["Id"]) + "rckipid=" + checkintoken + "\n")
