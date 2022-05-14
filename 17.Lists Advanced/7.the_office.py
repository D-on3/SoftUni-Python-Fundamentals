
em_happyness = input().split(' ')
factor = int(input())
em_happyness_int = list(map(int,em_happyness))
print(em_happyness_int)
filtered = filter(lambda em: em * factor, em_happyness_int)
print(filtered)

# print(f'Score: {happy_count}/{total_count}. Employees are happy!')
# print(f'Score: {happy_count}/{total_count}. Employees are not happy!')