# Stream Of Letters
line = input()
word_collection = ''
word = ''
c = False
o = False
n = False

while line != 'End':

    if line.isalpha():
        if (line == 'c' and c != True) or (line == 'o' and o != True) or (line == 'n' and n != True):
            if line == 'c':
                c = True
            if line == 'o':
                o = True
            if line == 'n':
                n = True
        else:
            word += line

    if c == True and o == True and n == True:
        word_collection += word + ' '
        c = False
        o = False
        n = False
        word = ''

    line = input()

print(word_collection)

