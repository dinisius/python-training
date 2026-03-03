import numpy as np

# Script for ordering digits from bigger to lesat

# Input from user

input = 44444

# Basically, my workflow was correct. In python to sort digits as first thing i should
# convert number to string format in order to have access to each digit. 
# Then I should convert each digit in str forma back to int and right after it
# convert it to list format. 
# There is a useful function map, each can convert str digits back to int.
list_of_digits = list(map(int, str(input))) 
print(list_of_digits)

# Then I sort it with function sort() and key word reverse. True, if i want decreasing order
list_of_digits.sort(reverse = True)
print(list_of_digits)

result = ''.join(map(str, list_of_digits))

result_python = ''.join(str(x) for x in list_of_digits)

print(result)
print(result_python)

'''
result = 0
for each in list_of_digits:
    result *= 10
    result = result + each

print(result)'''





