import re

text = input()

pattern = r" [a-zA-Z\d]+[\._-]*[a-zA-Z\d]+@[a-zA-Z]+-*[a-zA-Z]+(\.+[a-zA-Z]+-?[a-zA-Z]+)+"

emails = re.finditer(pattern, text)
for email in emails:
    print(email.group())