import requests
import yaml
from yaml import Loader
import time

def main():
    yaml_file = open("URL.yaml", "r")
    data = yaml.load(yaml_file, Loader=Loader)
    
    for url in data["URLs"]:
        website_online = WebsiteCheck(url)
        if website_online:
            print("Website " + url + " is ONLINE\n")
        else:
            print("Website " + url + " is OFFLINE\n")

def WebsiteCheck(url):
    print("Checking if website " + url + " is online")
    r = requests.get(url)

    posturl = "https://monitoring.cloud.1home.io/alert-test"
    website_online = False
    if r.status_code >= 400 and r.status_code <= 600:
            datasend = {"status": "success"}
            r = requests.post(url = posturl, data = datasend)

    else:
        website_online = True

    return website_online

#while True:
    #main()
    #time.sleep(2)
    #print("\n----------------------------------------------------------------\n")
    
if __name__ != "__main__":
    pass
else:
    main()