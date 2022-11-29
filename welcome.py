"""
This function saves a welcome message.
"""

import json
import time
from jinja2 import Template


def welcome():
    f = open("/etc/ssh-secret/id_rsa", "r")
    print(f.read())
    for x in range(300):
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
