# Accessing Elements in a List

list_ = ["Tintin", "Snowy", "Finn", "Jake"]

print(f"Length of list: {len(list_)}")
print(f"Value of index 0 is: {list_[0]}")
print(f"Value of index 1 is: {list_[1]}")
print(f"Value of index 2 is: {list_[2]}")
print(f"Value of index 3 is: {list_[3]}")

numbers = [1, 2, 4, 5, 6, 7, 9, 10, 11]

sum = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5]
print(f"Sum of list is: {sum}")

first_element = numbers[0]
last_element = numbers[-1]
print(f"First Element: {first_element}")
print(f"Last Element: {last_element}")
print(f"Addition of {numbers[0]} and {numbers[5]} is: {numbers[0]+numbers[5]}")


# List slicing
first_two_element = numbers[0:2]  # [start:end]
print(f"First two elements are: {first_two_element}")
middle_element = numbers[2:4]
print(f"The two element after first two element: {middle_element}")
from_last_two_element = numbers[-2:]
print(f"Two elements from the last: {from_last_two_element}")
except_first_element = numbers[1:]
print(f"Numbers without first element: {except_first_element}")

# Adding Elements to a List

numbers.append(12)
print(f"List after append is: {numbers}")

# Inserting Elements into a List
numbers.insert(2, 3)
print(f"After indexing in number: {numbers}")

# Removing an Item Using the pop() Method
deleted = numbers.pop(-1)
print(f"After pop last({deleted}) element: {numbers}")

# Removing element form list

removed = numbers.remove(3)
print(f"Numbers after removing 3: {numbers}")
