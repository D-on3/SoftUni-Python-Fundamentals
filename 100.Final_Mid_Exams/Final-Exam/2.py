import re

pattern = r"(.+)>(?P<numbers>\d{3})\|(?P<lower>[a-z]{3})\|(?P<upper>[A-Z]{3})\|(?P<symbols>[^<>]{3})<\1"

n = int(input())

for _ in range(n):
    line = input()
    matches = re.search(pattern, line)
    if not matches:
        print("Try another password!")
    else:
        obj = matches.groupdict()
        password = ""
        password += obj['numbers']
        password += obj['lower']
        password += obj['upper']
        password += obj['symbols']
        print(f"Password: {password}")

















