numbers = [1, 2, 3, 4]

# The line `numbers_v2 = list(map(lambda i : i * 2, numbers))` is creating a new list called
# `numbers_v2` by applying a lambda function to each element in the `numbers` list. The lambda
# function takes an input `i` and multiplies it by 2. The `map()` function applies this lambda
# function to each element in the `numbers` list, and the `list()` function converts the result into a
# list. So, `numbers_v2` will contain the elements of `numbers` multiplied by 2.
numbers_v2 = list(map(lambda i : i * 2, numbers))

print(numbers_v2)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = (list(map(lambda x, y : x + y, numbers_1,numbers_2 )))

print(result)