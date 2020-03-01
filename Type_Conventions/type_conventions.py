birth_year = input('What is your birth year? ')
# age = 2020 - birth_year # Throws type convention error
print(type(birth_year))
age = 2020 - int(birth_year)

print(age)
print(type(age))

# Assignment pounds to kilos
weight_in_pounds = input('What is your weight(in lbs) ? ')

weight_in_kilos = int(weight_in_pounds) / 2.205

print('Weight in pounds :: ' + weight_in_pounds)
print('Weight in kilos :: ' + str(weight_in_kilos))
