
number_of_numbers = int(input())
# even = list()
# odd = list()
# positive = list()
# negative =  list()
number_list = list()
filtered = list()

for num in range(number_of_numbers):
    current_num = int(input())
    number_list.append(current_num)
    # if current_num % 2 == 0 or current_num == 0:
    #     even.append(current_num)
    #     if current_num < 0:
    #         negative.append(current_num)
    #     elif current_num >=0:
    #         positive.append(current_num)
    # elif current_num % 2 != 0 :
    #     odd.append(current_num)
    #     if current_num < 0:
    #         negative.append(current_num)
    #     elif current_num >=0:
    #         positive.append(current_num)


command = input()
for current_num in number_list:
    if command == 'even' and current_num % 2 == 0:
        filtered.append(current_num)
    elif command == 'odd'and current_num % 2 != 0:
        filtered.append(current_num)
    elif command == 'postive' and current_num >= 0:
        filtered.append(current_num)
    elif command == 'negative' and current_num  0:
        filtered.append(current_num)

print(filtered)
