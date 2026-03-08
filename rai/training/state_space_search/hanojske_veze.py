import numpy as np
import matplotlib as plt

# DFS implementation

a = 1
b = 2
c = 3

pomoc_vektor = [a, b, c]

first_sloup = [a, b, c]
second_sloup = []
third_sloup = []

goal = [a, b, c]
moves = [second_sloup, third_sloup, first_sloup]

sloup = {a:first_sloup, b:first_sloup, c:first_sloup} # key = disk, value = number of sloup

last_move = [0, 0, 0]

find_solution = False

def check_positions(kolik):
    if kolik[0] > kolik[1]:
        print("Out of rules!")
        return False
    else:
        print("Move is acceptable")
        return True
        
def check_if_we_are_not_here(disk, iteration):
    if disk not in moves[iteration]:
        return True
    else:
        print("We are already here. Try next move")
        return False
    
def check_is_there_anything_above(number):
    if sloup[number].index(number) is not 0:
        return False
    else:
        return True
    
failed = 0
number_of_disk = 0

dva = 2

nula = 0

he = 1

# ZKUS PROHODIT PODMINKY

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
            
            current_disk = pomoc_vektor[number_of_disk]

            if check_is_there_anything_above(current_disk):
                pass
            else:
                number_of_disk += 1
                continue

            if check_if_we_are_not_here(sloup[current_disk][nula], moves.index(move)):
                pass
            else:
                check_if_we_are_not_here(sloup[current_disk][nula], moves.index(move))
                failed += 1
                break

            move.insert(0, sloup[current_disk][nula])

            if len(move) > 1:
                if check_positions(move):
                    pass
                else:
                    check_positions(move)
                    move.pop(nula)
                    branch_end = True
                    failed += 1
                    break
            
            sloup[current_disk].pop(nula)
            sloup[current_disk] = move


            if c in third_sloup and he == 1:
                dva = 1
                pomoc_vektor.pop()
                he = 0


            number_of_disk += 1
            failed = 0
        
            
            



# moves[i].append(second_sloup[0])