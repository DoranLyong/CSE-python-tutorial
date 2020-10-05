"""
[ref] https://codeup.kr/problem.php?id=1058

Question:
    1. take two true(1) or false(0) 
    2. print true when all are Flase 
"""
import sys 

x, y = map(int, sys.stdin.readline().rstrip().split())
x, y = map(bool, [x, y])


XnorGate = lambda x, y: not(x or y)

print(int(XnorGate(x, y)))




"""
not A and not B  -> not(A or B)
"""