import requests
import yaml
from yaml import Loader

datasend = {"status": "success"}

num = 0

yaml_file = open("URL.yaml", "r")
data = yaml.load(yaml_file, Loader=Loader)

posturl = "https://monitoring.cloud.1home.io/alert-test"

while True:
    r = requests.get(data["URLs"][num])

    print(r.ok)
    print(r.status_code)
    print(data["URLs"][num])

    if r.status_code >= 400 and r.status_code <= 600:
        print("Spletna stran ne deluje!")
        r = requests.post(url = posturl, data = datasend)
    else:
        print("Spletna stran deluje!")

    print(datasend)
    response = r.text
    #print("The response is:%s" %response)
    num = num + 1
    if num == len(data["URLs"]):
        break