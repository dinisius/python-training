import numpy as np

input_string = str(num)

length = len(input_string)

list_of_digits = []

sort = []

k = 0 

while k < length:
    list_of_digits.append(int(input_string[k]))
    k += 1

l = length

l -= 2

pomoc = 0
pokus = False
indexes = []

while l >= 0:

    k = l

    maximum = list_of_digits[0]
    minimum = list_of_digits[1]

    index_max = 0
    index_min = 1

    if maximum > minimum:
        True
    elif maximum < minimum:
        temp_value = minimum
        temp_index = index_min
        minimum = maximum
        index_min = index_max
        maximum = temp_value
        index_max = temp_index
    else:
        break

    start_to_check = 2

    while k > 0:

        if len(list_of_digits) > 3:
            if list_of_digits[start_to_check] > maximum:
                maximum = list_of_digits[start_to_check]
                index_max = start_to_check
            elif list_of_digits[start_to_check] < minimum:
                minimum = list_of_digits[start_to_check]
                index_min = start_to_check
            else:
                False
            k -= 1
            start_to_check += 1
        else:
            if list_of_digits[start_to_check] > maximum:
                maximum = list_of_digits[start_to_check]
                index_max = start_to_check
            elif list_of_digits[start_to_check] < minimum:
                minimum = list_of_digits[start_to_check]
                index_min = start_to_check
            else:
                pokus = True
                break

    indexes.extend([index_max, index_min])
    for ind in sorted(indexes, reverse=True):
        del list_of_digits[ind]
    indexes.clear()

    if not pokus:
        sort.insert(0+pomoc, maximum)
        sort.insert(1+pomoc, minimum)
        pomoc += 1
    else:
        sort.insert(0+pomoc, maximum)
        sort.insert(1+pomoc, minimum)
        sort.insert(1+pomoc, list_of_digits[0])


    l -= 2

result = 0

for number in sort:
    result *= 10
    result += number   

num = result


