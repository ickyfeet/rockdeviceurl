# rockdeviceurl
Generates URLs for RockRMS check in devices

Requires:
    
    requests

Pass the following arguments at the commandline, all are required:

* -u Your Rock URL (Example:  https://rock.hillsidewired.com)
* -k Your Rock API key
* -t Your Rock check in user token that will allow auto login

Usage:

python3 rockdeviceurl -u 'https://rock.example.com' -k 'Rock API Key' -t 'Check in user token'
