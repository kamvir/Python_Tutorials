title = '============================== Formatted Strings =============================='

print(title)

note = 'Please refer code for better understanding'

firstName = 'John'

lastName = 'Smith'

# Normal string
message = firstName + ' [' + lastName + '] is a coder'

# Formatted string
msg = f'{firstName} [{lastName}] is a coder'

print(message, ':: Normal String')

print(msg, ':: Formatted String')

print('Note :: ' + note)

print(title)
