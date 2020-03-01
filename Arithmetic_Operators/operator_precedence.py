title = '========================= Operators Precedence ========================='

description = '''
# Order of precedence
# 1. Parenthesis >> (10 + 3)
# 2. exponential >> 10 ** 2
# 3. multiplication or division
# 4. addition or subtraction
'''

note = 'Note :: Please refer code for better understanding.'

print(title)

print(description)

print('Here are some few examples below :: ')

num = 10 + 3 * 2

print('10 + 3 * 2 =', num)  # Outputs :: 16

num2 = 10 + 3 * 2 ** 2

print('10 + 3 * 2 ** 2 =', num2)  # Outputs :: 22

# Assignment

num3 = (2 + 3) * 10 - 3

print('(2 + 3) * 10 - 3 =', num3)  # Outputs :: 47

print(note)

print(title)
