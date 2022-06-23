overall = 0
for worker in range(3):
    current_worker = int(input())
    overall += current_worker
number_of_students= int(input())
actual_students = number_of_students
hours = 0
while actual_students > 0:
    hours +=1
    actual_students -= overall
    if hours % 4 == 0:
        hours += 1

print(f'Time needed: {hours}h.')