name_input = input().split(', ')

sorted_names = sorted(name_input)
sorted_names = sorted(sorted_names, key=lambda names: -len(names))

print(sorted_name)