# There are some values in other data types that conditions will consider
# equivalent to True and False.
# When used in conditions, 0, 0.0, and '' (the empty string) are
# considered False, while all other values are considered True.

name = ''
while name:  # same as: while not name != ''
    print('Enter your name:')
    name = input()

print('How many quests will you have?')
numOfGuests = int(input())
if numOfGuests:  # same as: numOfGuests != 0
    print('Be sure to have enough room for all your guests.')

print('Done')
