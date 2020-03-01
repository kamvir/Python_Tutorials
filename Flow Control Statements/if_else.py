title = '========================= if Statements ========================='

note = 'Note :: Please refer code for better understanding.'

print(title)

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

# Assignment

price = 1000000

has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print('Down Payment :: $' + str(down_payment))

print(note)

print(title)
