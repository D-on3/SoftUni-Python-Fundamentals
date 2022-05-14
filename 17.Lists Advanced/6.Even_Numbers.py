


numbers = input().split(', ')
numberss = list(map(int, numbers))
even_num = []
#TODO: ne gotovo
#even_num = map(lambda num:,numbers)

for i in range(len(numbers)):
    if numberss[i] % 2 == 0:
        even_num.append(i)


print(numbers)
print(numberss)