import numpy as np

# Script for ordering digits from bigger to lesat

# Input from user

tests = [0, 5, 10, 111, 1002, 987654321, 4441214]

for t in tests:

    input = t

    # Convert input in int format to str in order to easier processing digit-by-digit (at least i think so)
    input_string = str(input)

    # Extract the length of list. Why? It will help in comparing process and control iteration number
    length = len(input_string)

    # List of digits, where I will bank each digit, but in int format. Some sort of a inverse converting. 
    # At least now I think that is is reasonable step
    list_of_digits = []

    # List, where I will put sorted digits
    sort = []

    # Just helping variable
    k = 0 

    # Try to rewrite it with for

    # Fill list with input_string contest but in int format
    while k < length:
        list_of_digits.append(int(input_string[k]))
        k += 1

    # Don't know why, but why not? Use l instead of length
    l = length
    if length == 1:
        print("Length of input is 1")
        print(input)
    

    # Substract 2 from l because every itteration will process two digits in the lis_of_digits list, 
    # so it is not necessary to iterate whole list's length 
    # (At least now for me it is working solution)
    l -= 2

    # Help to fill sort list with sorted digits
    # Variable is zero in the beginning but is increased by one after every filling
    # So after first filling maximum-maximum and minimum-minimum of list_of_digits
    # are at 0 at 1 positions respectively. After pomoc += 1 I fill next maximum 
    # and minimum between maximum-maximum and minimum-minimum, and I repeat it before there is 
    # only last digit in the list
    pomoc = 0
    result = 0

    # Help to identify, that there is only last digit in the list
    pokus = False

    # Help to delete found maximum and minimum 'at once' by means of their indexes without.
    # Try to inplement reverse delete without for cyklus, seems that it would help  
    indexes = []
    kontrola = 0

    # Iterate while l is equal or bigger that 0
    # When substracting 2 from l:
        # in case l is even number -> after the last iteration l is equal to 0 -> stop iterating;
        # in case l is odd number -> after the last iteration l is equal to -1 -> stop iterating;

    while l >= 0:

        length = len(list_of_digits)
        k = l
        increment = 2

        maximum = list_of_digits[0]
        minimum = list_of_digits[1]

        index_max = 0
        index_min = 1

        if maximum > minimum:
            pass
        elif maximum < minimum:
            temp_value = minimum
            temp_index = index_min
            minimum = maximum
            index_min = index_max
            maximum = temp_value
            index_max = temp_index
        else:

            while increment != (length):
                minimum = list_of_digits[increment]
                index_min = increment
                increment += 1

                if maximum > minimum:
                    break
                elif maximum < minimum:
                    temp_value = minimum
                    temp_index = index_min
                    minimum = maximum
                    index_min = index_max
                    maximum = temp_value
                    index_max = temp_index
                    break
                
            if increment == (length):
                print('Error')
                for number in list_of_digits:
                    sort.insert(0+pomoc, number)
                    pomoc += 1
                break


            if 0:
                sort = list_of_digits
                for number in sort:
                    result *= 10
                    result += number   
                    print(result)
                break
            #break

        start_to_check = increment

        while (length - increment) > 0:

            if len(list_of_digits) > 3:
                if list_of_digits[start_to_check] > maximum:
                    maximum = list_of_digits[start_to_check]
                    index_max = start_to_check
                elif list_of_digits[start_to_check] < minimum:
                    minimum = list_of_digits[start_to_check]
                    index_min = start_to_check
                else:
                    print('Nothing is changed')
                increment += 1
                start_to_check += 1
            else:
                if list_of_digits[start_to_check] > maximum:
                    maximum = list_of_digits[start_to_check]
                    index_max = start_to_check
                elif list_of_digits[start_to_check] < minimum:
                    minimum = list_of_digits[start_to_check]
                    index_min = start_to_check
                else:
                    print('Well well well')
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


    print(sort)

if l != 1:
    for number in sort:
        result *= 10
        result += number   
        print(result)






'''
if l > 0:
        True
    else:
        print('list is empty')
        break   
    
'''  



