def at_least_one_true(a, b):
    return a or b
print(at_least_one_true(True, False)) 
print(at_least_one_true(False, False))
print(at_least_one_true(True, True))
print(at_least_one_true(False, True))