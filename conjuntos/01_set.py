# The code is creating a set called `set_countries` with three elements: 'Col', 'Mex', and 'Bol'. It
# then prints the set and the type of the set.
set_countries = {'Col', 'Mex', 'Bol'};
print(set_countries)
print(type(set_countries))

# The code is creating a set called `set_numbers` with five elements: 1, 2, 2, 44, and 23. However,
# since sets do not allow duplicate elements, the second occurrence of the number 2 is ignored. The
# code then prints the set `set_numbers`.
set_numbers = {1, 2, 2, 44, 23}
print(set_numbers)


# The code is creating a set called `set_types` with four elements: the integer 1, the string 'hola',
# the boolean value False, and the float 12.12. The code then prints the set `set_types`.
set_types = {1, 'hola', False, 12.12}
print(set_types)

# The code `set_from_string = set('hola')` is creating a set called `set_from_string` with the
# individual characters of the string 'hola' as its elements. The `set()` function is used to convert
# the string into a set. The code then prints the set `set_from_string`, which will output `{'h', 'o',
# 'l', 'a'}`.
set_from_string = set('hola')
print(set_from_string)

# The code is creating a set called `set_from_tuples` by converting a tuple `('abc', 'cbv', 'as')`
# into a set using the `set()` function. The resulting set will contain the three elements from the
# tuple: 'abc', 'cbv', and 'as'. The code then prints the set `set_from_tuples`.
set_from_tuples = set(('abc', 'cbv', 'as'))
print(set_from_tuples)

# The code is creating a list called `numbers` with seven elements: 1, 2, 3, 1, 2, 3, and 4. It then
# creates a set called `set_numbers` by converting the list `numbers` into a set using the `set()`
# function. Since sets do not allow duplicate elements, the duplicate numbers in the list are removed
# in the set. Finally, the code prints the set `set_numbers`, which will output `{1, 2, 3, 4}`.
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

# The code is creating a new list called `unique_numbers` by converting the set `set_numbers` into a
# list using the `list()` function. This will remove any duplicate elements from the set and create a
# list with only unique elements. Finally, the code prints the `unique_numbers` list.
unique_numbers = list(set_numbers)
print(unique_numbers)