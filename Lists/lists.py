title = "========================= Lists in Python ========================="

note = "Note :: Please refer code for better understanding"

print(title)

names = ['Viraj', 'Akash', 'Atit', 'Anurag', 'Omkar', 'Rohan']

print(names)  # Outputs :: ['Viraj', 'Akash', 'Atit', 'Anurag', 'Omkar', 'Rohan']

print(names[0])  # Outputs :: Viraj

print(names[-1])  # Outputs :: Rohan

print(names[2:])  # Outputs :: ['Atit', 'Anurag', 'Omkar', 'Rohan']

print(names[2:4])  # Outputs :: ['Atit', 'Anurag']

names[0] = 'Vkviraj'

print(names)  # Outputs :: ['Vkviraj', 'Akash', 'Atit', 'Anurag', 'Omkar', 'Rohan']

# Assignment

numbers = [3, 6, 2, 8, 4, 10]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

print(note)

print(title)
