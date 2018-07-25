# While the string in message is short in this example, it could be millions of characters long
# and the program would still run in less than a second.
# A similar program that finds phone numbers using regular expressions would also run in less than a second,
# but regular expressions make it quicker to write these programs.


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


# print('415-555-4242 is a phone number')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number.')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'


# On each iteration of the for loop, a new chunk of 12 characters from message is assigned to the variable chunk.
# For example, on the first iteration, i is 0, and chunk is assigned message[0:12] (that is, the string 'Call me at 4')
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# While there are several steps to using regular expressions in Python, each step is fairly simple.
# 1. Import the regex module with import re.
# 2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
# 3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object (mo).
# 4. Call the Match object’s group() method to return a string of the actual matched text.

import re


def isPhoneNumberRegex(text):
    #phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumberRegex = re.compile('(\d){3}-(\d){3}-(\d){4}')
    mo = phoneNumberRegex.search(text)
    print('Phone number found: ' + mo.group())


isPhoneNumberRegex('My number is 415-555-4242.')
