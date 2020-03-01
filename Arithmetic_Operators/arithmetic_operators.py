title = '==================================== Arithmetic Operators in Python ===================================='

print(title)

note = 'Note :: Please refer code for better understanding.'

print(10 + 3)  # Outputs :: 13 >> Addition

print(10 - 3)  # Outputs :: 7 >> Subtraction

print(10 * 3)  # Outputs :: 30 >> Multiplication

print(10 / 3)  # Outputs :: 3.3333333333333335 >> Division with float value as o/p

print(10 // 3)  # Outputs :: 3 >> Division with integer value as o/p. // is used for getting integer

print(10 % 3)  # Outputs :: 1 >> Modulus >> For getting remainder

print(10 ** 3)  # Outputs :: 1000 >> Exponential

x = 10

x = x + 3

print(x, ' :: Normal assignment')  # Outputs :: 13

y = 10

y += 3  # Outputs :: 13 >> Augmented assignment operator

print(y, ' :: Augmented assignment operator')

# ======================= Operators precedence =======================

# Order of precedence
# 1. Parenthesis >> (10 + 3)
# 2. exponential >> 10 ** 2
# 3. multiplication or division
# 4. addition or subtraction

num = 10 + 3 * 2

print(num)  # Outputs :: 16

num2 = 10 + 3 * 2 ** 2

print(num2)  # Outputs :: 22

# Assignment

num3 = (2 + 3) * 10 - 3

print(num3)  # Outputs :: 47

# ======================= Operators precedence =======================

print(note)

print(title)
