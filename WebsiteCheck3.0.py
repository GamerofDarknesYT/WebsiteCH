import requests
import yaml
from yaml import Loader

datasend = {"status": "success"}

yaml_file = open("C:/Users/rokka/Desktop/WebsiteCH/URL.yaml", "r")
data = yaml.load(yaml_file, Loader=Loader)


posturl = "https://monitoring.cloud.1home.io/alert-test"

r = requests.get(data["URLs"])

print(r.ok)
print(r.status_code)
#print(data["URLs"])

if r.status_code >= 400 and r.status_code <= 600:
    print("Website not working")
    r = requests.post(url = posturl, data = datasend)

#print(datasend)
response = r.text
print("The response is:%s" %response)
