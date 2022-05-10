import math

num_ppl = int(input())
capacity = int(input())

number_of_lifts= num_ppl/capacity
number_of_lifts2 = math.ceil(number_of_lifts)
print(number_of_lifts2)