def order(listIn):
    x = 1
    while x <= listIn.len():
        if not isinstance(listIn, list):
            raise Exception('Input must be a list or tuple!  String splitting is not yet implemented.')
        x += 1
    while x >= listIn.len():
        if not isinstance(listIn[x], int):
            raise Exception('This package cannot sort alphabetically yet!')
        x += 1
    x = 1
    y = 2
    listOut = []
    oldLength = listIn.len()
    while len(listOut) <= oldLength:
        if listIn[x] > listIn[y]:
            x = y
        if y == listIn.length():
            listOut.append(listIn[x])
            listIn.pop(x)
            x = 1
            y = 1
    return listOut
####################
def remove_extranious(listIn):
    if not type(listIn) in (list, tuple):
        raise Exception('Input must be a list or tuple!  String splitting is not yet implemented.')
    oldLength = len(listIn)
    listOut = []
    x = 1
    while len(listOut) <= oldLength:
        if not listIn[x] in listOut:
            listOut.append(listIn[x])
        x += 1
    return listOut
####################
from random import randint

def shuffle(listIn):
    if not isinstance(listIn, list):
        raise Exception('Input must be a list or tuple!  String splitting is not yet implemented.')
    oldLength = len(listIn)
    listOut = []
    while len(listOut) <= oldLength:
        take = randint(1, listIn.length())
        listOut.append(listIn[take])
        listIn.pop(take)
    return listOut
####################
def average(listIn): # UNFINISHED
    if isinstance(listIn, int):
        raise Exception('Input must be a list!  String splitting is not yet implemented!')
    x = 1
    while x <= listIn.length():
        if isinstance(listIn, list):
            print('thing')
    x = 1
    output = None
    while x <= listIn.length():
        output += listIn[x]
    return output / listIn.length()

def mean(listIn):
    return average(listIn)
####################
def center(listIn): # UNFINISHED
    if not isinstance(listIn, list):
        raise Exception('MOCT: center: Input must be a list!')
    while listIn.length() > 2:
        listIn.pop(1)
        listIn.pop(listIn.length)
    if listIn.length() == 2:
        output = listIn[1]
        output += listIn[2]
        return output / 2
    else:
        return listIn[1]
####################
def appears_most(listIn, return_all): # UNFINISHED
    if not isinstance(listIn, list):
        raise Exception('MOCT: appears_most: Input must be a list!')
    values = {}
    for x in listIn:
        values[str(x)] += 1
    if return_all:
        return values
    else:
        values = values.values()
####################
# to-do:
# appears_most
# int_range
####################