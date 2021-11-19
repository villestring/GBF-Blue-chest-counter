def addString(num1, num2):
# assumption: num1 has more or same digits as num2
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    i = len(num1) - 1
    diff = len(num1) - len(num2)
    rounding = 0
    result = ''

    while i >= diff:
        digit = int(num1[i]) + int(num2[i-diff]) + rounding
        rounding = digit // 10
        digit %= 10
        result = str(digit) + result
        i -= 1

    while i >= 0:
        if not rounding:
            result = num1[:i+1]+result
            return result
        digit = int(num1[i]) + rounding
        rounding = digit // 10
        digit %= 10
        result = str(digit) + result
        i -= 1

    if rounding > 0:
        result = '1' + result
    return result

def minusString(num1, num2):
    # if num1 < num2, just return '0'
    if len(num1) < len(num2) or num1 == num2:
        return '0'

    i = len(num1) - 1
    diff = len(num1) - len(num2)
    rounding = 0
    result = ''

    while i >= diff:
        digit = int(num1[i]) - int(num2[i-diff]) - rounding
        rounding = 1 if digit < 0 else 0
        digit = 10+digit if digit < 0 else digit
        result = str(digit) + result
        i -= 1
    while i >= 0:
        if not rounding:
            result = num1[:i+1]+result
            return result
        digit = int(num1[i]) - rounding
        rounding = 1 if digit < 0 else 0
        digit = 10+digit if digit < 0 else digit
        result = str(digit) + result
        i -= 1
    if rounding > 0:
        return '0'
    return result.lstrip('0')
