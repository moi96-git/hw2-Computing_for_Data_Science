

def dictionary_maker(param: []):
    output = {}
    for val1, val2 in param:
        output[val1] = val2
    return output

if __name__ == "__main__":
    test1= [('foo', 1), ('bar', 3), ('hi', 5)]
    print(dictionary_maker(test1))