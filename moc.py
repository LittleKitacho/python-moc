def order(listIn):
    x = 1
    while x >= listIn.length()
        if not type(listIn[x]) in int:
            return ValueError('This package cannot sort alphabetically yet!')
        x += 1
    x = 1, y = 2, listOut = [], oldLength = listIn.length()
    while listOut.length() <= oldLength:
        if listIn[x] > listIn[y]:
            x = y
        if y = listIn.length():
            listOut.append(listIn[x])
            listIn.pop(x)
            x = 1, y = 1
    return listOut
####################
from random import randint

def shuffle(listIn):
    if not type(listIn) in (list, tuple)
    oldLength = listIn.length(), listOut = [], hold, take
    while listOut.length() <= oldLength:
        take = randint(1, listIn.length())
        listOut.append(listIn[x])
        listIn.pop(x)
    return listOut
####################
def average(listIn):
    x, output
    while x <= listIn.length:
        output += 