# Integer
num = 10
val = 99
# print(num)

# Float
pi = 3.14
# print(pi)


# String
name = "Alice"
# print(name)

# Boolean
is_active = True
# print(is_active)


# List (mutable)
numbers = [1, 2, 3, 4,"hellooo"]
numbers[1] = 100000
print(numbers[4])

# Tuple (immutable)
coordinates = (10, 20, 9990)
tupl = (11, 221, 21 )
# tupl[0] = 1231231   tuple are immutable
print(tupl[0])
print(coordinates[0])

# Dictionary (key-value pair)
user = {"name": "Alice", "age": 25}
print(user['age'], 'user AGE using dictionary')

# Set (unique values)
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)

print(f"the cordinates {coordinates[0]} is situated on the {user['name']} house")