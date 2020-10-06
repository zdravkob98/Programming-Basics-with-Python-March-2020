line = input()
cc = 0
nn = 0
oo = 0
word = ''



while line != 'End' and  line != 'a' or line != 'b' or line != 'c'  or line != 'd' or line != 'e' or line != 'f' or line != 'g'  or line != 'h'  or line != 'i'  or line != 'j'  or line != 'k'  or line != 'l'  or line != 'm'  or line != 'o'  or line != 'p'  or line != 'q'  or line != 'r'  or line != 's'  or line != 't'  or line != 'u'  or line != 'v'  or line != 'w'  or line != 'x'  or line != 'y'  or line != 'z' :

    if line == 'a' or line != 'b' or line != 'c' or line != 'd' or line != 'e' or line != 'f' or line != 'g' or line != 'h' or line != 'i' or line != 'j' or line != 'k' or line != 'l' or line != 'm' or line != 'o' or line != 'p' or line != 'q' or line != 'r' or line != 's' or line != 't' or line != 'u' or line != 'v' or line != 'w' or line != 'x' or line != 'y' or line != 'z':
        if line == 'c' :
            if cc == 0:
                cc += 1
            else:
                cc == 1
                word += line
        elif line == 'n' :
            if nn == 0:
                nn += 1
            else:
                cc == 1
                word += line
        elif line == 'o' :
            if oo == 0:
                oo += 1
            else:
                oo == 1
                word += line
        elif cc == 1 and nn == 1 and oo == 1:
                cc = 0
                nn = 0
                oo = 0


        else:
            word += line
    line = input()
print(word)



