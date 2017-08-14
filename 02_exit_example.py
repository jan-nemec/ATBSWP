# How to terminate the program
# This always happens if the program execution reaches the bottom of the instructions.
# However, you can cause the program to terminate, or exit, by calling the sys.exit() function.
# Since this function is in the sys module, you have to import sys before your program can use it.

# from sys import exit
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
        # break
    print('You typed ' + response + '.')
