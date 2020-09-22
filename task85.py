def to_another_ns(num: int, count_system: int):
    """
    Converting integer to another numeral system (works only in sytems with base >= 10)
    :param num: integer to convert
    :param count_system: base of numeral system
    :return: Converted value
    """
    k = 0
    r = 0
    while num > 0:
        r += (num % count_system) * (10 ** k)
        k += 1
        num //= count_system
    return r


a = int(input())

# Base of numeral system
c = 8
# Converting input integer to another numeral system
converted_value = to_another_ns(a, c)

# Counting sum of all digits
num_sum = 0
while converted_value > 0:
    num_sum += converted_value % 10
    converted_value //= 10

# Converting it to another numeral system and sending to output
print(to_another_ns(num_sum, c))