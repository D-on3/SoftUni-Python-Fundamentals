def replace(raw_message, current, new):
    raw_message = raw_message.replace(current, new)
    print(raw_message)
    return raw_message


def cut(raw_message, start, end):
    if start > 0 or end < len(raw_message):
        print("Invalid indices!")
    else:
        if len(raw_message) > 0:
            raw_message = raw_message[:start] + raw_message[end + 1:]
            print(raw_message)
    return raw_message


def make(raw_message, case_sense):
    if case_sense == "Upper":
        raw_message = raw_message.upper()
    else:
        raw_message = raw_message.lower()
    print(raw_message)
    return raw_message


def check(raw_message, str):
    if str not in raw_message:
        print(f"Message doesn't contain {str}")
    else:
        print(f"Message contains {str}")
    return raw_message


def sum_idx(raw_message, start_i, end_i):
    if start_i > 0 and end_i < len(raw_message):
        sum_ascii = 0
        substring = raw_message[start_i:end_i + 1]
        for char in substring:
            sum_ascii += ord(char)
        print(sum_ascii)
    else:
        print("Invalid indices!")

    return raw_message


message = input()

decrypting_data = input()

while not decrypting_data == "Finish":
    data = decrypting_data.split()
    command = data[0]

    if command == "Replace":
        current_char = data[1]
        new_char = data[2]
        message = replace(message, current_char, new_char)
    elif command == "Cut":
        start_index = int(data[1])
        end_index = int(data[2])
        message = cut(message, start_index, end_index)
    elif command == "Make":
        case = data[1]
        message = make(message, case)
    elif command == "Check":
        string = data[1]
        message = check(message, string)
    elif command == "Sum":
        start_idx = int(data[1])
        end_idx = int(data[2])
        message = sum_idx(message, start_idx, end_idx)

    decrypting_data = input()