title = '==================== Comparison Operators ===================='

note = 'Note :: Please refer code for better understanding.'

print(title)

# greater than and lesser than

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Assignment

name = input("Enter name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")

print(note)

print(title)
