import requests
import yaml
from yaml import Loader

r = requests.get("https://monitoring.cloud.1home.io")
datasend = {"status": "success"}

posturl = "https://monitoring.cloud.1home.io/alert-test"

print(r.ok)
print(r.status_code)

if r.status_code >= 400 and r.status_code <= 600:
    print("Website not working")
    r = requests.post(url = posturl, data = datasend)

print(datasend)
response = r.text
print("The response is:%s" %response)

yaml_file = open("URL.yaml", "r")
data = yaml.load(yaml_file, Loader=Loader)

print(data)