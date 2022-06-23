def check_book_exist(books_list, book_searched):
    return True if book_searched in books_list else False


def add(books_list, book_add):
    if not check_book_exist(books_list, book_add):
        books_list.insert(0, book_add)
    return books_list


def take(books_list, book_take):
    if check_book_exist(books_list, book_take):
        books_list.remove(book_take)
    return books_list


def swap(books_list, book_1, book_2):
    if check_book_exist(books_list, book_1) and check_book_exist(books_list, book_2):
        index_1 = books_list.index(book_1)
        index_2 = books_list.index(book_2)
        books_list[index_1], books_list[index_2] = books_list[index_2], books_list[index_1]
    return books_list


def insert(books_list, book_insert):
    books_list.append(book_insert)
    return books_list


def check(books_list, idx):
    if not idx > len(books_list):
        print(books_list[idx])
    return books_list


books = input().split("&")

line = input().split(" | ")

while not line[0] == "Done":
    command = line[0]
    book_name = line[1]

    if command == "Add Book":
        books = add(books, book_name)
    elif command == "Take Book":
        books = take(books, book_name)
    elif command == "Swap Books":
        book_name_2 = line[2]
        books = swap(books, book_name, book_name_2)
    elif command == "Insert Book":
        books = insert(books, book_name)
    elif command == "Check Book":
        index = int(line[1])
        books = check(books, index)

    line = input().split(" | ")

print(', '.join(books))
