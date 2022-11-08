"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
4! = 1 x 2 x 3 x 4 = 24
"""


# Helper method to test equality
def equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'

# Todo: Create a function that produces the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n

# Todo: Test factorial function
equals(factorial(0), 1)
equals(factorial(1), 1)
equals(factorial(2), 2)
equals(factorial(4), 24)


# Todo: Request a number from the user
number = int(input("Enter a number: "))

# Todo: Print a list of factorials from 0 to the given number
factorial_list = []

for i in range(number + 1):
    factorial_list.append(factorial(i))

print(factorial_list)