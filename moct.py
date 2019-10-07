class typeTest:
    def __init__(listIn, )

def order(listIn):
    x = 1
    while x <= listIn.length():
        if not type(listIn) in (list, tuple):
            raise TypeError('Input must be a list or tuple!  String splitting is not yet implemented.')
    while x >= listIn.length()
        if not type(listIn[x]) in int:
            raise ValueError('This package cannot sort alphabetically yet!')
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
def remove_extranious(listIn):
    if not type(listIn) in (list, tuple):
        raise TypeError('Input must be a list or tuple!  String splitting is not yet implemented.')
    oldLength = listIn.length(), listOut = [], x = 1, y = 2
    while listOut.length() <= oldLength:
        if not x <= y:
        
        if y = oldLength
####################
from random import randint

def shuffle(listIn):
    if not type(listIn) in (list, tuple):
        raise TypeError('Input must be a list or tuple!  String splitting is not yet implemented.')
    oldLength = listIn.length(), listOut = [], hold, take
    while listOut.length() <= oldLength:
        take = randint(1, listIn.length())
        listOut.append(listIn[x])
        listIn.pop(x)
    return listOut
####################
def average(listIn):
    if type(listIn) in int:
        raise TypeError('Input must be a list!  String splitting is not yet implemented!')
    x = 1
    while x <= listIn.length():
        if type(listIn[x]) in (list, tuple)
    x = 1, output
    while x <= listIn.length():
        output += listIn[x]
    return output / listIn.length()

def mean(listIn):
    average(listIn)
####################
def center(listIn):

    while listIn.length() >= 2:
        listIn.pop(1)
        listIn.pop(listIn.length)
    if listIn.length() == 2:
        output = listIn[1]
        output += listIn[2]
        return output