number = int(input())

for i in range(number):
    for j in range(i+1):
        print("*", end='')
    print('')
for n in range(number-1,0,-1):
    for m in range(n):
        print("*", end='')
    print('')
