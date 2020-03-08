title = "=============== List methods ==============="

note = "Note :: Please refer code for better understanding"

print(title)

numbers = [5, 2, 1 , 7, 4]

numbers.append(20)  # Adds list item.

print(numbers)  # Outputs: [5, 2, 1, 7, 4, 20]

numbers.insert(0, 10)  # Inserting list item on a particular index

print(numbers)  # Outputs :: [10, 5, 2, 1, 7, 4, 20]

numbers.remove(5)  # Removes particular list item

print(numbers)  # Outputs :: [10, 2, 1, 7, 4, 20]

numbers.clear()  # Clears the list

print(numbers)  # Outputs :: []

numbers = [5, 2, 1, 7, 4]

numbers.pop()  # Pops the last element

print(numbers)  # Outputs :: [5, 2, 1, 7]

print(numbers.index(5))  # Outputs :: 0. Gives the index value of existing list item in list

# Commenting it because of throwing error.
# print(numbers.index(50))  # Throws error better to use 'in' operator

numbers = [5, 2, 1, 7, 4, 5]

print(numbers.count(5))  # Outputs :: 2. Gives no. of occurrence of particular list item in list.

numbers.sort()  # For sorting lit items in list. Sorts in Ascending Order

print(numbers)  # Outputs :: [1, 2, 4, 5, 5, 7]

# For descending order

numbers.sort()
numbers.reverse()

print(numbers)  # Outputs :: [7, 5, 5, 4, 2, 1]

copied_numbers = numbers.copy()  # For copying list. Also an independent list.

print(copied_numbers)  # Outputs :: [7, 5, 5, 4, 2, 1]

# Assignment :: Remove duplicate items

num_list = [1, 2, 3, 4, 4, 5, 6, 6]

uniques = []

for number in num_list:
    if number not in uniques:
        uniques.append(number)

print(uniques)  # Outputs :: [1, 2, 3, 4, 5, 6]

print(note)

print(title)
