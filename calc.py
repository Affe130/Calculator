'''
calc.py Version: 1.0 by Affe_130
Important:
   This program should be runned in a console with the py command!
Help:
   Modes: -add, -sub, -mul, -div, -exp, -root, -stat, Example: py calc.py -add 1 2 3
'''

import sys

arg = sys.argv
values = []

for i in range(2, len(arg)): #Adds all values in the argument list to a different list
    values.append(arg[i])
    
def add(list): #Adds all values
    result = float(list[0])
    for i in range(1, len(list)):
        result = result + float(list[i])
    return result

def sub(list): #Takes the first value and subtracts it with all the others
    result = float(list[0])
    for i in range(1, len(list)):
        result = result - float(list[i])
    return result
 
def mul(list): #Multiplicates all values
    result = float(list[0])
    for i in range(1, len(list)):
        result = result * float(list[i])
    return result
    
def div(list): #Takes the first value and divides it with all the others
    result = float(list[0])
    for i in range(1, len(list)):
        result = result / float(list[i])
    return result

def exp(list): #Takes the first value to the power of the second value
    result = float(list[0]) ** float(list[1])
    return result

def root(list): #Takes the root from the first value of the second value
    exp = 1 / float(list[1])
    result = float(list[0]) ** exp
    return result   

#All these ifs check for which argument has been given

if len(arg) <= 1: #No argument has been given
    print("-help to get help with commands")

if len(arg) > 1:
    if arg[1] == "-add":
        print("Answer: ", add(values))

    if arg[1] == "-sub":
        print("Answer: ", sub(values))

    if arg[1] == "-mul":
        print("Answer: ", mul(values))

    if arg[1] == "-div":
        print("Answer: ", div(values))

    if arg[1] == "-exp":
        print("Answer: ", exp(values))

    if arg[1] == "-root":
        print("Answer: ", root(values))

    if arg[1] == "-stat":
        values.sort()
        print("Number of values: ", len(values))
        print("Total value: ", add(values))
        print("Highest value: ", values[len(values) - 1])
        print("Lowest value: ", values[0])
        print("Average value: ", add(values) / len(values))
    
    if arg[1] == "-help":
        print("Modes: -add, -sub, -mul, -div, -exp, -root, -stat, Example: py calc.py -add 1 2 3")




    
    

    
