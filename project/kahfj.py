import string
symbols = string.digits + string.ascii_uppercase

number = input('Enter a number you need to convert: ')
old_base = int(input('Enter old base: '))
new_base = int(input('Enter new base: '))


def _int_to_base(number, new_base):  # converts to needed base from decimal
    sign = -1 if number < 0 else 1
    number *= sign
    ans = ''
    while number:
        ans += symbols[number % new_base]
        number //= new_base
    if sign == -1:
        ans += '-'
    return ans[::-1]


def convert(number, old_base, new_base, precision=None):
    # converting from original base to decimal
    integral, point, fractional = number.strip().partition('.')
    num = int(integral + fractional, old_base) * old_base ** -len(fractional)

    # from decimal to new base
    precision = len(fractional) if precision is None else precision
    s = _int_to_base(int(round(num / new_base ** -precision)), new_base)
    if precision:
        return s[:-precision] + '.' + s[-precision:]
    else:
        return s


# def addition(a, b, old_base):  # adds numbers
#     a1 = convert(a, old_base, 10)
#     b1 = convert(b, old_base, 10)
#     sum1 = a1 + b1
#     return convert(sum1, 10, old_base)
#
#
# def subtraction(a, b, old_base):  # subtracts numbers
#     a1 = convert(a, old_base, 10)
#     b1 = convert(b, old_base, 10)
#     sum1 = a1 - b1
#     return convert(sum1, 10, old_base)
#
#
# def multiplication(a, b, old_base):  # multiplicands numbers
#     a1 = convert(a, old_base, 10)
#     b1 = convert(b, old_base, 10)
#     sum1 = a1 * b1
#     return convert(sum1, 10, old_base)
#
#
# def division(a, b, old_base):  # divines numbers
#     a1 = convert(a, old_base, 10)
#     b1 = convert(b, old_base, 10)
#     sum1 = a1 / b1
#     return convert(sum1, 10, old_base)
#
#
# def power(a, b, old_base):  # a powers b
#     a1 = convert(a, old_base, 10)
#     b1 = convert(b, old_base, 10)
#     sum1 = a1 ** b1
#     return convert(sum1, 10, old_base)

print(convert(number, old_base, new_base))


