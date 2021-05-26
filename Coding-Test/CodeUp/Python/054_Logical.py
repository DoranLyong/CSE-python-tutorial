"""
[ref] https://codeup.kr/problem.php?id=1054

Question:
    1. take two true(1) or false(0) 
    2. print true when all are true 
"""
import sys 

x, y = map(int, sys.stdin.readline().rstrip().split())
x, y = map(bool, [x, y])


AndGate = lambda x, y: x and y 

print(int(AndGate(x, y)))