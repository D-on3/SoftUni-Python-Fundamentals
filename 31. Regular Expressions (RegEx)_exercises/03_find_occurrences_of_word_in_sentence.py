import re

text = input()
word = input()

pattern = r"\b" + re.escape(word) + r"\b"

matches = len(re.findall(patter, text, re.IGNORECASE))


print(matches)