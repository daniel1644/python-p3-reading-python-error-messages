#!/usr/bin/env python3

assert(2 + 2 == 4)  # This will pass because the condition is true

##....
assert(1 == 1)  # This will pass because the condition is true


##...
def divide(a, b):
    assert b != 0, "The divisor b cannot be zero"
    return a / b

print(divide(10, 2))  # This will pass
# print(divide(10, 0))  # This will raise an AssertionError


