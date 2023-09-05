import re

email = input("Whats your email").strip()

#if "@" and "." in email:

'''
username, domain = email.split("@")

if username and "." in domain:
'''

if re.search(r"^\w+@\w+\.\w+$", email, re.IGNORECASE):

    print("Valid")
else:
    print("Invalid")

