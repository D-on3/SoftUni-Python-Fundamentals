def sum_numbers(arg,arg2):
    global sum_of
    sums = []
    sums.append(arg)
    sums.append(arg2)
    sum_of = sum(sums)

sum_numbers(int(input()),int(input()))


def subtract(arg3):
    result = sum_of - arg3
    print(result)

subtract(int(input()))

