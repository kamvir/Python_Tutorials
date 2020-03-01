title = '==================== Logical Operators ===================='

note = 'Note :: Please refer code for better understanding.'

print(title)

has_high_income = False

has_good_credit = True

has_criminal_record = False

# Logical 'and' operator
if has_high_income and has_good_credit:
    print("Eligible for loan")

# Logical 'or' operator
if has_high_income or has_good_credit:
    print("Eligible for loan")

# Logical 'not' operator

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


print(note)

print(title)
