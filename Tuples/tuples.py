title = "===================== Tuples in Python ====================="

note = "Note: Please refer code for better understanding"

print(title)

numbers = (1, 2, 3)

print(numbers[0])  # Outputs :: 1

# numbers[0] = 2  # Throws error: 'tuple' object does not support item assignment

# Unpacking

coordinates = (1, 2, 3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# Can also be written as
x, y, z = coordinates

print(x, y, z)  # Outputs: 1 2 3

print(note)

print(title)
