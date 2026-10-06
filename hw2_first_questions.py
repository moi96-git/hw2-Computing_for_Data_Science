# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#

def triple(x):
    return x * 3

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#

def subtract(a, b):
    return a - b

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3), ('hi', 5)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly


def dictionary_maker(param: []):
    output = {}
    for val1, val2 in param:
        output[val1] = val2
    return output

if __name__ == "__main__":
    test1= [('foo', 1), ('bar', 3), ('hi', 5)]
    print(dictionary_maker(test1))