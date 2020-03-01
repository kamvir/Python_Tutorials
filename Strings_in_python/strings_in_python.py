title = '============================= Strings in Python ============================='

print(title)

note = 'Please refer code for better understanding'

course = 'Python for Beginners'

print(course)

course = "Python's Course for Beginners"

print(course)

course = 'Python for "Beginners"'

print(course)

course = '''
Hi John,

Here is our first email to you.

Thank you,
VkTechs Pvt Ltd
'''
print(course)

course = 'Python for Beginners'

print(course[-2], ' :: String character at index "-2"')

# ===================================== showing string on a particular range ===================================== #
print(course[0:3], ' :: 0-3')  # Outputs :: Pyt

print(course[1:], ' :: 1-length of string')  # Outputs :: ython for Beginners

print(course[:5], ' :: 0-5')  # Outputs :: Pytho

print(course[:], ' :: creates a copy of string')  # Outputs :: Python for Beginners

another = course[:]  # copy of course variable

print(another, ' :: copied variable')

# Assignment

name = 'Jennifer'

print(name[1:-1])  # Outputs :: ennife

# ===================================== showing string on a particular range ===================================== #

print('Note :: ' + note)

print(title)
