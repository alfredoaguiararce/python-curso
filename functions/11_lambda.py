def increment(x):
    """
    The function `increment` takes a number as input and returns that number incremented by 1.
    
    :param x: The parameter "x" is a variable that represents a number
    :return: the value of `x` incremented by 1.
    """
    return x + 1

result = increment(10)
print(result)

# The line `increment_v2 = lambda x : x + 1` is creating an anonymous function (also known as a lambda
# function) that takes a parameter `x` and returns `x + 1`. The lambda function is then assigned to
# the variable `increment_v2`.
increment_v2 = lambda x : x + 1

result = increment_v2(20)
print(result)

# The code is creating an anonymous function (lambda function) called `full_name` that takes two
# parameters `name` and `last_name`. The function returns a formatted string that combines the
# capitalized versions of `name` and `last_name` with the text "Fullname is".
full_name = lambda name, last_name : f'Fullname is {name.title()} {last_name.title()}'
text = full_name("alfredo","aguiar")
print(text)