import __init__ as moct

testList = [1, 2, 3, 4, 3, 5, 6, 9, 8, 7]

# Test moct.order function
try:
    result = moct.order(testList)
except Exception as error:
    raise Exception('Order returned an error')
else:
    if (result != [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]):
        raise Exception('Order returned wrong result, expected [1, 2, 3, 3, 4, 5, 6, 7, 8, 9], got '..result)
    else:
        print('Order function tested sucsessfully.')

try:
    result = moct.remove_extranious(testList)
except Exception as error:
    raise Exception('remove_extranious', testList, )
else:
    if result != [1,2,3]