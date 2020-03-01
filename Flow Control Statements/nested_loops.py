title = "====================== Nested Loops in Python ======================"

note = "Note :: Please refer code for better understanding"

print(title)

for x in range(4):
    for y in range(4):
        print("(" + str(x) + ", " + str(y) + ")")

# Challenge

numbers = [5, 2, 5, 2, 2]  # For printing 'F'

# numbers = [1, 1, 1, 1, 5]  # For printing 'L'

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print(note)

print(title)
