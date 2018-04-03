#!/usr/bin/python
import sys

def execute_program(code, braces, cells, aCells, p):
    instr_pointer = 0
    output = ""

    while instr_pointer < len(code):
        command = code[instr_pointer]
        
        if command == "+": aCells[p] += 1 if aCells[p] < 255 else 0
        elif command == "-": aCells[p] -= 1 if aCells[p] > 0 else 0
        elif command == "<":
            p -= 1
            if len(aCells) >= cells:
                print ("Reached cells limit: " + str(cells))
                print ("Last state:")
                print (aCells)
                sys.exit(1)
            if p < 0: 
                aCells.insert(0, 0)
                p = 0
        elif command == ">":
            p += 1
            if len(aCells) >= cells:
                print ("Reached cells limit: " + str(cells))
                print ("Last state:")
                print (aCells)
                sys.exit(1)
            if p == len(aCells): aCells.append(0)
        elif command == ".": output += chr(aCells[p])
        
        #TODO
        # elif command == ","

        elif command == "[":
            if aCells[p] == 0:
                instr_pointer = braces[instr_pointer] 
        else:
            if aCells[p] != 0:
                instr_pointer = braces[instr_pointer] 
        instr_pointer += 1
    return (output, aCells, p)

def get_braces(code):
    stack = list()
    final = dict()

    for index in range(0, len(code)):
        if code[index] == "[":
            stack.append(index)
        elif code[index] == "]":
            startBrace = stack.pop()
            final[startBrace] = index
            final[index] = startBrace
        index += 1
    return final

###########################################################

def process_string(code, pointer, cells):
    content = list()
    content = filter(lambda x: x in ["+", "-", "<", ">", ".", ",", "[", "]"], code)
    content = list(content)
    output, cells,p = execute_program(content, get_braces(content), 300000, cells, pointer)
    result = "Stack:\t\t" + str(cells) + "\nPointer:\t" + str(p) + "\nOutput:\t\t" + output
    return result, p, cells
