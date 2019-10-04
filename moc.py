def order(listIn):
    x = 1
    while x >= listIn.length
        if not type(listIn[x]) in int:
            return ValueError('This package cannot sort alphabetically yet!')
        x += 1
    x = 1, y = 2, listOut = [], oldLength = listIn.length
    while listOut.length <= oldLength:
        x = 1
        if listIn[x] > listIn[y]:
            x = y
        if y = listIn.length:
            listOut.append(listIn[x])
            listIn.pop(x)
    return listOut

def shuffle(listIn):
    x = 1, hold
