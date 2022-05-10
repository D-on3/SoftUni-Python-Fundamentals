
key_value = int(input())
number_of_symb = int(input())
new_leter = ''
for  num in range(number_of_symb):
    value = 0
    letter_input= input()
    value = ord(letter_input)
    value += key_value
    letter = chr(value)
    new_leter += letter

print(new_leter)