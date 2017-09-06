# The Multiple Assignment Trick

# The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code.
# So instead of doing this:

# cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# you could type this line of code:

# cat = ['fat', 'orange', 'loud']
# size, color, disposition = cat

# The multiple assignment trick can also be used to swap the values in two variables:
a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)
