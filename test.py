import moct

testList = [1, 2, 3, 4, 3, 5, 6, 9, 8, 7]

# Test moct.order function
try:
    result = moct.order(testList)
except Exception as error:
    raise Exception('MOCT encountered an error when ordering!  {}'.format(error))
else:
    if (result != [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]):
        raise Exception('MOCT does not return expected output when ordering!')
    else:
        print('Order function tests completed sucsessfully.')
        print('No faults were found.')