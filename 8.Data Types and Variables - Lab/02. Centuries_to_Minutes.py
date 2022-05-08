import math
number_of_cent = int(input())

convert_to_years = number_of_cent * 100
convert_to_days = math.trunc(convert_to_years * 365.2422)
convert_to_hours = convert_to_days * 24
convert_to_minutes = convert_to_hours * 60

print(f'{number_of_cent} centuries = {convert_to_years} years = {convert_to_days} days = {convert_to_hours} '
      f'hours = {convert_to_minutes} minutes')