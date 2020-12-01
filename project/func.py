s = input()
a = int(input())
b = int(input())


def half1(x, b):
    assert (x >= 0)
    assert (1 < b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r


def half2(s, b):
    assert (1 < b < 37)
    return int(s, b)


def convert(s, a, b):
    return half1(half2(s, a), b)


print(convert(str(s), a, b))
