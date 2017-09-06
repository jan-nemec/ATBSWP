spam = ['apples', 'bannanas', 'tofu', 'cats']


def convertToString(items):
    text = ''
    for item in items:
        if item == items[-1]:
            text += 'and ' + item
        else:
            text += f'{item}, '
    return text


result = convertToString(spam)
print(result)
