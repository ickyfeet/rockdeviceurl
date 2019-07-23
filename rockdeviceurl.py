import requests
import json
import argparse


# Initialize argparse
parser = argparse.ArgumentParser()

parser.add_argument(
    "-u",
    "--url",
    required=True,
    type=str,
    help="Rock base url. Example: https://rock.example.com",
)

parser.add_argument("-k", "--key", required=True, type=str, help="Rock api key.")

parser.add_argument("-t", "--token", required=True, type=str, help="Rock user token")

# Assign arguments to args
args = parser.parse_args()


apiheaders = {"Content-Type": "application/json", "Authorization-Token": args.key}

kiosk_url = (
    args.url + "/api/Devices?$filter=IPAddress ne null and DeviceTypeValueId eq 41"
)

getkiosks = requests.get(kiosk_url, headers=apiheaders)

parsed = json.loads(getkiosks.text)

for i in parsed:
    print(
        i["Name"]
        + "\n"
        + args.url
        + "/checkin?Kioskid="
        + str(i["Id"])
        + "&rckipid="
        + args.token
        + "\n"
    )
