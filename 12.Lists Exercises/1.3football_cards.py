
usr_input = input().split(' ')
a_team = 11
b_team = 11
counter_a = 0
counter_b = 0
player_losses = []
is_over = False
for el in usr_input:
    if el not in player_losses:
        player_losses.append(el)
        if 'A' in el:
            a_team -= 1
            counter_a += 1
        elif 'B' in el:
            b_team -= 1
            counter_b += 1
    if a_team < 7 or b_team < 7:
        is_over = True
        break

print(f'Team A - {11- counter_a}; Team B - {11-counter_b}')
if is_over:
    print(f'Game was terminated')