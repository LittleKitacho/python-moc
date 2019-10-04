import moc

testList = [1, 2, 3, 4, 3, 5, 6, 9, 8, 7]

if moc.order == [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]:
    raise SystemError('\'moc\' returns wrong value when tested!')