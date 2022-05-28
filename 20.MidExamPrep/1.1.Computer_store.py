

command = input()
net_sum = 0
total_price = 0
while command != 'special' and command != 'regular':
    price = float(input())

    if command > 0 :
        net_sum += price
    else:
        print('Invalid price!')
    
