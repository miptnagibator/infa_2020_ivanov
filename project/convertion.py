import string
symbols = string.digits + string.ascii_uppercase



def convert(number, old_base, new_base, precision=None):

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




