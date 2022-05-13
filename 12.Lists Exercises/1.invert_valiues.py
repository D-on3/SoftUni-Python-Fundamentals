

some_values = input().split(' ')

new_list = []

for value in some_values:
    if value == '0':
        new_list.append(int(value))
    else:
        if int(value) > 0 :
            new_list.append(-int(value))

        elif int(value) < 0:
            new_list.append(abs(int(value)))

print(new_list)