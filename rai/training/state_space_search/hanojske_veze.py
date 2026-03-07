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

sloup = {a:first_sloup, b:first_sloup, c:first_sloup} # key = number of sloup, value = disk

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
    if number.index is not 0:
        return False
    else:
        return True
    
failed = 0

while(find_solution == False):

    for move in moves:

        if failed > 2:
            pomoc += 1
        
        if(find_solution == True):
            break

        branch_end = False

        while(branch_end == False):

            if pomoc > 2:
                pomoc = 0

            if failed > 2:
                failed = 0
            
            current_disk = pomoc_vektor[pomoc]

            if check_if_we_are_not_here(sloup[current_disk][pomoc], move):
                pass
            else:
                check_if_we_are_not_here(sloup[current_disk][pomoc], move)
                failed += 1
                break


            if check_is_there_anything_above(sloup[current_disk][pomoc]):
                pass
            else:
                branch_end = True
                failed += 1
                break

            move.append(sloup[current_disk][pomoc])

            if len(move) > 1:
                if check_positions(move):
                    pass
                else:
                    check_positions(move)
                    move.pop()
                    branch_end = True
                    failed += 1
                    break
            
            sloup[current_disk].pop(pomoc)
            sloup[current_disk] = move

            pomoc += 1
        
            
            



# moves[i].append(second_sloup[0])