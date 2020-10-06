fave_book = input()
capacity = int(input())

book_checked = 0

book_found = True

while book_found:
    current_book = input()
    if fave_book == current_book:
        print(f'You checked {book_checked} books and found it.')
        book_found = False

    book_checked += 1
    if book_checked == capacity:
        break
if book_found:
    print('The book you search is not here!')
    print(f'You checked {book_checked} books.')