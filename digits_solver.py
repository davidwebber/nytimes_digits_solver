#!/usr/bin/env python

"""
https://www.nytimes.com/games/digits

The digits puzzle in nytimes gives six integers with the goal of reaching a 
"target" integer using sequential operations of +,-,*,/.
The resulting number must be a positive integer, so certain operations with "-"
or / are not allowed.
You do not have to use all the numbers.

Test case:
    1, 2, 3, 5, 10, 25
    target 74

Without considering optimizations such as commutation,
A brute-force search will require
6*5*4 = 120 1st round
5*4*4 =  80 2nd round
4*3*4 =  48 3rd round
3*2*4 =  24 4th round
2*1*4 =   8 5th round
"""

# TODO make a cool iterator for the numbers and operators
# eg for i,j,op in iterate(pool):

from typing import List

def valid_operation(i: int, j: int, op: str):
    if op == "-" and i < j:
        return False
    if op == "/" and j == 0:
        return False
    if op == "/":
        x = i/j
        return x == int(x)
    return True

def add(i:int, j:int):
    return i+j

def sub(i:int, j:int):
    return i-j

def mul(i:int, j:int):
    return i*j

def div(i:int, j:int):
    return int(i/j)

op_to_fun = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":div}

def operate(pool: List[int], target: int, breadcrumbs: List[str]):
    print("    "*len(breadcrumbs), pool, breadcrumbs)
    if target in pool:
        return breadcrumbs
    if len(pool) < 2:
        return False
    operations = ["+","-","*","/"]
    for i in range(len(pool)):
        for j in range(1,len(pool)):
            if i==j:
                continue
            x, y = pool[i], pool[j]
            newpool = pool.copy()
            newpool.remove(x)
            newpool.remove(y)
            for op in operations:
                #print(i,j,op)
                if not valid_operation(x, y, op):
                    continue
                z = op_to_fun[op](x,y)
                #print(pool, breadcrumbs, "{}{}{}".format(x,op,y))
                result = operate(newpool+[z], target, breadcrumbs[:]+["{}{}{}".format(x,op,y)])
                #print("internal",result)
                if result != False:
                    return result
    return False           


if __name__ == "__main__":
    #pool, target = [1,2,3,5,10,25], 74
    #pool, target = [3,5,8,9,11,20], 259
    pool, target = [3,5,7,19,23,25], 458
    #pool, target = [1,2,4], 8

    breadcrumbs = []
    result = operate(pool, target, breadcrumbs)
    print("Done!",result)

