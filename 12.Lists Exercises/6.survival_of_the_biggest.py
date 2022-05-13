
usr_input = input().split(' ')
copy_nums =list(map(int, usr_input))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    usr_input.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(', '.join(usr_input))