import re

pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"

line = input()

result = [el.group() for el in re.finditer(pattern, line)]

print(",".join(result))