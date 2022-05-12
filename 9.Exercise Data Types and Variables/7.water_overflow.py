
number_of_pouring = int(input())

volume_of_tank = 255
filled_volume = 0
for pour in range(number_of_pouring):
    volume_poured = int(input())
    if volume_poured+filled_volume <= volume_of_tank:
        filled_volume += volume_poured
    else:
        print('Insufficient capacity!')


print(filled_volume)