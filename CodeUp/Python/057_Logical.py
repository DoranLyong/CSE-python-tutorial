"""
[ref] https://codeup.kr/problem.php?id=1057

Question:
    1. take two true(1) or false(0) 
    2. print true when they are the same 
"""
import sys 

x, y = map(int, sys.stdin.readline().rstrip().split())
x, y = map(bool, [x, y])


XnorGate = lambda x, y: x == y

print(int(XnorGate(x, y)))




"""
(not A and not B) or (A and B)
"""