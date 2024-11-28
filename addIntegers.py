def _padding(a, b):
    if len(a)<len(b):
        smaller = a
        larger = b
    elif len(b)<len(a):
        smaller = b
        larger = a
    else:
        return a, b
    c = smaller[0] + ((len(larger)-len(smaller))*"0") + smaller[1:]
    return larger, c

def _getLarger(a, b):
    for i in range(1, len(a)):
        if int(a[i]) > int(b[i]):
            return a, b
        elif int(a[i]) < int(b[i]):
            return b, a
    return a, a

def _add(a, b):
    sign = a[0]
    carry = 0
    result = ""
    i = len(a)-1
    while i>0:
        s = str(int(a[i]) + int(b[i]) + carry)
        if len(s)>1:
            result += s[1]
            carry = int(s[0])
        else:
            result += s[0]
            carry = 0
        if i == 1:
            result += str(carry) + sign
        i -= 1
    return result[::-1]

def _subtract(a, b):
    sign = a[0]
    carry = 0
    result = ""
    i = len(a)-1
    while i>0:
        s = int(a[i]) + carry
        if s < int(b[i]):
            carry = -1
            result += int(s + 10 - int(b[i]))
        else:
            carry = 0
            result += str(s - int(b[i]))
        i -= 1
    return result[::-1]


def addIntegers(a, b):
    if len(a)<2 or len(b)<2:
        return "Enter valid Intergers to sum"
    elif len(a)<6 and len(b)<6:
        return str(int(a) + int(b))
    a, b = _padding(a, b)
    if a[0] == b[0]:
        return _add(a, b)
    else:
        larger, smaller = _getLarger(a, b)
        if larger == smaller:
            return "0"
        return _subtract(larger, smaller)
# Test Case 1: Both numbers are positive and of equal length
print(addIntegers("+12345678", "+87654321"))  # Expected output: "+99999999"

# Test Case 2: Both numbers are negative and of equal length
print(addIntegers("-12345678", "-87654321"))  # Expected output: "-99999999"

# Test Case 3: Different signs with the first number larger in magnitude
print(addIntegers("+12345678", "-1234567"))   # Expected output: "+11111111"

# Test Case 4: Different signs with the second number larger in magnitude
print(addIntegers("-1234567", "+12345678"))   # Expected output: "+11111111"

# Test Case 5: Different signs with numbers of equal magnitude
print(addIntegers("+12345678", "-12345678"))  # Expected output: "0"

# Test Case 6: One number is shorter than the other
print(addIntegers("+12345678", "+123"))       # Expected output: "+12345801"

# Test Case 7: One number is small and both have different signs
print(addIntegers("+1000", "-500"))           # Expected output: "+500"

# Test Case 8: Very large numbers
print(addIntegers("+123456789012345678", "+876543210987654321"))  # Expected output: "+999999999999999999"

# Test Case 9: Invalid input (too short)
print(addIntegers("+1", "-123"))              # Expected output: "Enter valid Intergers to sum"

# Test Case 10: Both numbers are short and simple addition
print(addIntegers("+5", "+5"))                # Expected output: "10"

# Test Case 11: Both numbers are negative and one is shorter
print(addIntegers("-12345678", "-123"))       # Expected output: "-12345801"

# Test Case 12: Same magnitude but opposite signs
print(addIntegers("+5000", "-5000"))          # Expected output: "0"
