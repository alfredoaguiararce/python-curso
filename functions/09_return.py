def find_volume(length=1, width=1, depth=1):
    """
    The function calculates the volume of a rectangular object given its length, width, and depth.

    :param length: The length parameter represents the length of an object or space. It has a default
    value of 1 if no value is provided when calling the function, defaults to 1 (optional)
    :param width: 1, defaults to 1 (optional)
    :param depth: The depth parameter represents the depth or height of an object, defaults to 1
    (optional)
    :return: three values: the volume (length * width * depth), the width, and the string 'hola'.
    """
    return length * width * depth, width, 'hola'

# The code is calling the `find_volume` function with the argument `width=10`. The function returns
# three values: the volume (length * width * depth), the width, and the string 'hola'.
result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)