import __init__ as moct

testList = [1, 2, 3, 4, 3, 5, 6, 9, 8, 7]

# Test moct.order function
try:
    result = moct.order(testList)
except Exception as error:
    raise Exception('Order returned an error while executing: '+error)
else:
    if (result != [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]):
        raise Exception('Order returned wrong result, expected [1, 2, 3, 3, 4, 5, 6, 7, 8, 9], got '+str(result))
    else:
        print('Order function tested succsessfully.')

try:
    result = moct.remove_extranious(testList)
except Exception as error:
    raise Exception('Remove Extranious returned an error while executing:/n'+error)
else:
    if result != [1, 2, 3, 4, 5, 6, 9, 8, 7]:
        raise Exception('Remove Extranious returned wrong result, expected [1, 2, 3, 4, 5, 6, 9, 8, 7], got '+str(result))
    else:
        print('Remove Extranious tested out succsessfully')

try:
    result = moct.shuffle(testList)
except Exception as error:
    raise Exception('Shuffle returned an error while executing:\n'+error)
else:
    if result == [1, 2, 3, 4, 3, 5, 6, 9, 8, 7]:
        raise Exception('Shuffle returned wrong result, expected something other than [1, 2, 3, 4, 3, 5, 6, 9, 8, 7] but got '+str(result))
    else:
        print('Shuffle tested out succsessfully')

try:
    result = moct.mean(testList)
except Exception as error:
    raise Exception('Mean returned an error while executing:\n'+error)
else:
    if result != 4.8:
        raise Exception('Mean returned wrong result.\nExpected 4.8, got '+str(result))
    else:
        print('Mean tested out succsessfully')

try:
    result = moct.median(testList)
except Exception as error:
    raise Exception('Medain returned an error while executing:\n'+error)
else:
    if result != 
