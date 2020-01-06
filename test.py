class ReturnValueError(ValueError):
    def __init__ (self, function, expected, returned):
        self.message = "Testing fault in "+function
        self.explanation = "Result expected was "+expected+" but result returned was "+returned+"."

class MoctException(Exception):
    def __init__ (self, function, input_, error):
        self.message = "MOCT encounterd an exception in "+function
        self.explanation = "Gave "+input_+" got back "+error+"."

import __init__ as moct

testList = [1, 2, 3, 4, 3, 5, 6, 9, 8, 7]

# Test moct.order function
try:
    result = moct.order(testList)
except Exception as error:
    raise Exception('Order returned an error')
else:
    if (result != [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]):
        raise ReturnValueError('order', [1,2,3,3,4,5,6,7,8,9], result)
    else:
        print('Order function tested sucsessfully.')

try:
    result = moct.remove_extranious(testList)
except Exception as error:
    raise MoctException('remove_extranious', testList, )
else:
    if result != [1,2,3]