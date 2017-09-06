import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concetrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful'
            ]

print(messages[random.randint(0, len(messages) - 1)])

# Python uses references whenever variables must store values of mutable data types,
# such as lists or dictionaries.
# For values of immutable data types such as strings, integers, or tuples,
# Python variables will store the value itself.
