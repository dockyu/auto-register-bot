from mailtm import Email
from threading import Thread
import sys
import time

def listener(message):
    content = message['text']
    for line in content.splitlines():
        if 'Verification Code' in line: # find line with verification code
            # split "Verification Code: f9de1c6f404b95a005cb58656ff4c415"
            code = line.split(": ")[1]
            print(code)
            return code
            
    

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register(username='tttttt6', password=None, domain='bugfoo.com')
email_address = str(test.address)
print("\nEmail Adress: " + email_address)

# Start listening
test.start(listener)
print("\nWaiting for new emails...")

time.sleep(5)
exit()