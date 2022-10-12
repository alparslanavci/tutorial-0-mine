"""
This function saves a welcome message.
"""

import json
from jinja2 import Template


def welcome():
    print("This is a test log")
    template = Template('Welcome to {{ name }}!')
    message = template.render(name='Orquestra')

    message_dict = {
        "message": message,
        "schema": "message"
    }

    with open("welcome.json", 'w') as f:
        f.write(json.dumps(message_dict, indent=2))  # Write message to file as this will serve as output artifact
