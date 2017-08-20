# If you try to use a local variable in a function before you assign a value to it,
# as in the following program, Python will give you an error.


def spam():
    print(eggs)  # Error!
    eggs = 'spam local'


eggs = 'global'
spam()

# This error happens because Python sees that there is an assignment statement for eggs in the spam() function
# and therefore considers eggs to be local.
# But because print(eggs) is executed before eggs is assigned anything,
# the local variable eggs doesn’t exist. Python will not fall back to using the global eggs variable.
