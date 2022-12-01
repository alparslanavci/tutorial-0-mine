"""
This function saves a welcome message.
"""

import json
import time
import requests
from jinja2 import Template


def welcome():
    f = open("/app/iam/passport", "r")
    print(f.read())

    r=requests.get("http://config-service.config-service:8099/api/config/secrets", headers={"Authorization":"Bearer " + f.read()})
    print("JSON Response ", r.json())
    for x in range(1):
        print("Log " + str(x))
        time.sleep(1)
    template = Template('Welcome to {{ name }}!')
    message = template.render(name='Orquestra')

    message_dict = {
        "message": message,
        "schema": "message"
    }

    with open("welcome.json", 'w') as f:
        f.write(json.dumps(message_dict, indent=2))  # Write message to file as this will serve as output artifact
