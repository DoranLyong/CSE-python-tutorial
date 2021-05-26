"""
[ref] https://codeup.kr/problem.php?id=1055

Question:
    1. take two true(1) or false(0) 
    2. print true when any of them is True at least
"""
import sys 

x, y = map(int, sys.stdin.readline().rstrip().split())
x, y = map(bool, [x, y])


OrGate = lambda x, y: x or y 

print(int(OrGate(x, y)))

