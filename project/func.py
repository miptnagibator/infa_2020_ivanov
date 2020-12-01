number = input("Число:")
old_system = int(input("Старая система: "))
new_system = int(input("Новая система: "))


class number():
    def __init__(self):
        self.num = 0
        self.base = 0

    def plus(self, object):
        pass

    def minus(self, object):
        pass

    def mult(self, object):
        pass

    def divide(self, object):
        pass


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


print(convert(str(number), old_system, new_system))
