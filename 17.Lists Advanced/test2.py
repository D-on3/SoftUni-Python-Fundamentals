state= input().split('|')

command = input().split(' ')
while "Yohoho!" not in command:

    if 'Loot' in command:
        command.pop(0)
        for item in command:
            if item not in state:
                state.insert(0,item)

    elif 'Drop' in command:
        command.pop(0)
        for index in command:
            lfuf = state.pop(int(index))
            lfuf = state.append(lfuf)
            print(state)
    elif 'Steal' in command:
        command.pop(0)
        for steal in  command:
            state.pop(int(steal))
            print(state)
    command = input().split(' ')

print(state)
