def increment(x):
    """
    The function `increment` takes a number as input and returns that number incremented by 1.
    
    :param x: The parameter "x" is a variable that represents a number
    :return: the value of x incremented by 1.
    """
    return x + 1


def high_order_func(x, func):
    """
    The high_order_func takes a value x and a function func, and returns the sum of x and the result of
    applying func to x.
    
    :param x: A number or value that will be passed as an argument to the function `func`
    :param func: A function that takes a single argument and returns a value
    :return: the sum of the input value `x` and the result of applying the input function `func` to `x`.
    """
    return x + func(x)

# The code is creating two lambda functions.
increment_v2 = lambda x : x + 1
hof_v2 = lambda x, func : x + func(x)

#  2 + (2 + 1) = 5
result = high_order_func(2, increment)
print(result)

result_v2 = hof_v2(2, increment_v2)
print(result_v2)

