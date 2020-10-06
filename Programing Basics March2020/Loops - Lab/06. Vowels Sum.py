word = input()
word_len = len(word)

sum = 0

for i in range(0, word_len):
    letter = word[i]
    if letter == 'a':
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == 'o':
        sum += 4
    elif letter == 'u':
        sum += 5

print(sum)

