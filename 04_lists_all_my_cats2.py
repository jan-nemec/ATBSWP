# Instead of using multiple, repetitive variables, you can use a single variable that contains a list value.
# For example, here’s a new and improved version of the allMyCats1.py program.
# This new version uses a single list and can store any number of cats that the user types in.

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation

print('The cat names are:')
for name in catNames:
    print(' ' + name)

# The benefit of using a list is that your data is now in a structure,
# so your program is much more flexible in processing the data than it would be with several repetitive variables.
