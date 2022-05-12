

sum_lists = input().split(', ')
number_of_beggars = int(input())
final_list = []
counter_of_index = 0
temp_sum = 0
sum_lists_as_digits = []

for index in range(len(sum_lists)):
    sum_lists_as_digits.append(int(sum_lists[index]))

while counter_of_index < number_of_beggars:
    for el in range(counter_of_index,len(sum_lists_as_digits),number_of_beggars):
        temp_sum += sum_lists_as_digits[el]

    final_list.append(temp_sum)
    counter_of_index += 1
    temp_sum = 0

print(final_list)