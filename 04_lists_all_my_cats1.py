# It turns out that this is a bad way to write code. For one thing,
# if the number of cats changes, your program will never be able to store more cats than you have variables.
# These types of programs also have a lot of duplicate or nearly identical code in them.
# Consider how much duplicate code is in the following program

print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1, catName2, catName3, catName4, catName5, catName6)
