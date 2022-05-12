
n= int(input())
negative = []
positive = []
all_in = []
count_positive= 0
for i in range(n):
    curren_number= int(input())
    if curren_number >= 0:
        positive.append(curren_number)
        count_positive +=1
    else:
        negative.append(curren_number)

print(positive)
print(negative)
print(f"Count of positives: {count_positive}\nSum of negatives: {sum(negative)}")