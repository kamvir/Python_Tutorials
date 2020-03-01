title = "========================= For loop in Python ========================="

note = "Note :: Please refer code for better understanding"

print(title)
# Looping in a string
for price in 'Python':
    print(price)

# Looping in list
print("Looping in list")

print("Looping in list :: Strings")

for price in ['Viraj', 'Rohini', 'Vinod']:
    print(price)

print("Looping in list :: Numbers")

for price in [1, 2, 3, 4]:
    print(price)

# Looping in a range

print("Looping in range")

print("Looping in range:: 0-9 i.e., range(10)")

for price in range(10):
    print(price)

print("Looping in range:: 5-9 i.e., range(5,10)")

for price in range(5, 10):
    print(price)

print("Looping in range:: 5-9 i.e., incrementing it by 2")

for price in range(5, 10, 2):
    print(price)

# Assignment

prices = [10, 20, 30]
totalPrice = 0

for price in prices:
    totalPrice += price

print("Total Price :: $" + str(totalPrice))

print(note)

print(title)
