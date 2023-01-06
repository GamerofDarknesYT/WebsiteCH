import requests
import yaml
from yaml import Loader

r = requests.get("https://monitoring.cloud.1home.io")

print(r.ok)
print(r.status_code)

if r.status_code >= 400 and r.status_code <= 600:
    print("Webside not working")

#yaml_file = open("URL.yaml", "r")
#data = yaml.load(yaml_file, Loader=Loader)

#print(data)