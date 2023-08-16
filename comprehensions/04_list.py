numbers = []
for element in range(1,11):
    numbers.append(element)

print(numbers)

# List Comprehensions
numbers = [element for element in range(1, 11)]
print(numbers)

# Pair numbers
pairs = [number * 2 for number in range(1,100) if number%2 == 0]
print(pairs)