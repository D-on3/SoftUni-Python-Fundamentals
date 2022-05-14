

def odd_even_sum(arg1):
    odd = 0
    even = 0
    for num in arg1:
        if int(num) % 2 == 0:
            even += int(num)
        else:
            odd += int(num)
    print(f'Odd sum = {odd}, Even sum = {even}')


odd_even_sum(input())