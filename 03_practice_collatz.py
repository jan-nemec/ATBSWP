# Chapter 3 | Practice Projects
# The Collatz Sequence

# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.


def collatz(number):
    if number % 2 == 0:
        # print(str(number) + ' // 2')
        return number // 2
    else:
        # print('3 * ' + str(number) + ' + 1 =', str(3 * number + 1))
        # print(f'3 * {number} + 1')
        return 3 * number + 1


# result = collatz(4)
# result = collatz(5)

value = None
while not value:
    try:
        value = int(input('Enter number: '))
    except ValueError:
        print('You must type in an integer!')

while value != 1:
    value = collatz(value)
    print(value)

value2 = int(input('Enter number2: '))

while True:
    value2 = collatz(value2)
    print(value2)
    if value2 == 1:
        break

print('Thank you!')
