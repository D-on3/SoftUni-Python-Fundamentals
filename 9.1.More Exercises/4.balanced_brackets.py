

lines = int(input())
counter = 0
for line in range(lines):
    usr= input()
    if usr in " ( ":
        counter += 1
    elif usr in " ) ":
        counter += 1

if counter % 2 != 0:
    print('UNBALANCED')
else:
    print('BALANCED')