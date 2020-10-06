line = input()
cc = 0
nn = 0
oo = 0
word = ''

word_sum = ''


while line != 'End':

    if line.isalpha():


        if line == 'c':
            if cc == 0:
                cc += 1
            else:
                cc == 1
                word += line
        elif line == 'n':
            if nn == 0:
                nn += 1
            else:
                cc == 1
                word += line
        elif line == 'o':
            if oo == 0:
                oo += 1
            else:
                nn == 1
                word += line

        else:
                word += line
        if cc == 1 and nn == 1 and oo == 1:
            word_sum += word + ' '
            word = ''
            cc = 0
            nn = 0
            oo = 0

    line = input()
print(f'{word_sum}')



