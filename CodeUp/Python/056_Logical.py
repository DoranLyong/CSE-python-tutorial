"""
[ref] https://codeup.kr/problem.php?id=1056

Question:
    1. take two true(1) or false(0) 
    2. print true when they are different 
"""
import sys 

x, y = map(int, sys.stdin.readline().rstrip().split())
x, y = map(bool, [x, y])


XorGate = lambda x, y: (x and not(y)) or (not(x) and y)

print(int(XorGate(x, y)))