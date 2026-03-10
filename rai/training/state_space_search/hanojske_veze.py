import numpy as np
import matplotlib as plt

# DFS implementation

a = 1
b = 2
c = 3

disk_bank = [a, b, c]

first_sloup = [a, b, c]
second_sloup = []
third_sloup = []

goal = [a, b, c]
moves = [second_sloup, third_sloup, first_sloup]

sloup = {a:first_sloup, b:first_sloup, c:first_sloup} # key = disk, value = number of sloup

find_solution = False

def check_positions(disk_on_sloup):
    if disk_on_sloup[0] > disk_on_sloup[1]:
        print("Out of rules!")
        return False
    else:
        print("Move is acceptable")
        return True
        
def check_if_we_are_not_here(disk, number_of_sloup):
    if disk not in moves[number_of_sloup]:
        return True
    else:
        print("We are already here. Try next move")
        return False
    
def check_is_there_anything_above(number_of_disk):
    if sloup[number_of_disk].index(number_of_disk) is not 0:
        return False
    else:
        return True
    
failed = 0
number_of_disk = 0
dva = 2

support = 1

while(find_solution == False):

    for move in moves:
        if failed > 2:
            number_of_disk += 1
        if(find_solution == True):
            break
        branch_end = False

        while(branch_end == False):

            if third_sloup == goal:
                print("YUPI!")
                find_solution = True
                break

            if number_of_disk > dva:
                number_of_disk = 0

            if failed > 2:
                failed = 0
            
            current_disk = disk_bank[number_of_disk]

            if check_is_there_anything_above(current_disk):
                pass
            else:
                number_of_disk += 1
                continue

            if check_if_we_are_not_here(sloup[current_disk][0], moves.index(move)):
                pass
            else:
                check_if_we_are_not_here(sloup[current_disk][0], moves.index(move))
                failed += 1
                break

            move.insert(0, sloup[current_disk][0])

            if len(move) > 1:
                if check_positions(move):
                    pass
                else:
                    check_positions(move)
                    move.pop(0)
                    branch_end = True
                    failed += 1
                    break
            
            sloup[current_disk].pop(0)
            sloup[current_disk] = move


            if c in third_sloup and support == 1:
                dva = 1
                disk_bank.pop()
                support = 0


            number_of_disk += 1
            failed = 0
        
            
            



# moves[i].append(second_sloup[0])