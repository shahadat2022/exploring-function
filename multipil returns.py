a = 40
b = 20
addition = a + b
subtraction = a - b

def add_sub(a, b):
    """
    This will Retuns two number addition and subtraction
    :param a: frist number
    :param b: second number
    :return:addition and subtraction
    """
    addition = a + b
    subtraction = a - b
    return addition, subtraction
result = addition, subtraction
print(add_sub.__doc__)
print(result)
print(type(result))


