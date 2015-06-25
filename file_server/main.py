print "Hello"

def max_value(a, b):
    if a > b:
        return a
    else:
        return b


def fr_dictionary(filename, open=open):
    f = open(filename, 'r')
    text = f.read()
    text = text.lower()
    d = {}
    for word in text.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    f.close()
    return d

print fr_dictionary('/home/z/pg1661.txt')
