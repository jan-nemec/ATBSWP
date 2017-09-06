# Passing References

# References are particularly important for understanding how arguments get passed to functions.
# When a function is called, the values of the arguments are copied to the parameter variables.
# For lists (and dictionaries, which I’ll describe in the next chapter),
# this means a copy of the reference is used for the parameter


def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

# Even though spam and someParameter contain separate references,
# they both refer to the same list.
# This is why the append('Hello') method call inside the function affects the list
# even after the function call has returned.

# Keep this behavior in mind:
# Forgetting that Python handles list and dictionary variables this way can lead to confusing bugs.
