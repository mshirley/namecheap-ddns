'''
Dynamic DNS service for Vultr
By Andy Smith
https://ajsmith.us/
https://github.com/andyjsmith/Vultr-Dynamic-DNS
'''

import json, requests
import netifaces as ni

# Import the values from the configuration file
with open("config.json") as config_file:
	config = json.load(config_file) # Convert JSON to Python

domain = config["domain"]
api_key = config["api_key"]
dynamic_records = config["dynamic_records"]

# Get the public IP of the server
ip = requests.get("https://ip.42.pl/raw").text

response = requests.get("https://dynamicdns.park-your-domain.com/update?host=lighthouse-ext-1&domain=plzhackmy.site&password={}&ip={}".format(api_key, ip))
