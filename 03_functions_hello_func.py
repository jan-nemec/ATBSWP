# A function is like a mini-program within a program.
# A major purpose of functions is to group code that gets executed multiple times.

# In general, you always want to avoid duplicating code,
# because if you ever decide to update the code—if, for example,
# you find a bug you need to fix—you’ll have to remember to change the code everywhere you copied it.

# As you get more programming experience,
# you’ll often find yourself deduplicating code, which means getting rid of duplicated or copy-and-pasted code.
# Deduplication makes your programs shorter, easier to read, and easier to update.


def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

# Functions as “Black Boxes”

# Often, all you need to know about a function are its inputs (the parameters) and output value;
# you don’t always have to burden yourself with how the function’s code actually works.
# When you think about functions in this high-level way, it’s common to say that you’re treating the function as a “black box.”

# This idea is fundamental to modern programming.
# Later chapters in this book will show you several modules with functions
# that were written by other people. While you can take a peek at the source code if you’re curious,
# you don’t need to know how these functions work in order to use them.
# And because writing functions without global variables is encouraged,
# you usually don’t have to worry about the function’s code interacting with the rest of your program.


# The hello() lines after the function are function calls.
# In code, a function call is just the function’s name followed by parentheses,
# possibly with some number of arguments in between the parentheses.
# When the program execution reaches these calls,
# it will jump to the top line in the function and begin executing the code there.
# When it reaches the end of the function, the execution returns to the line
# that called the function and continues moving through the code as before.
hello()
hello()
hello()
