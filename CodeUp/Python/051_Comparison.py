"""
[ref] https://codeup.kr/problem.php?id=1051

Question:
    1. take two integers; (a, b)
    2. a <= b -> print 1 
    3. a > b -> print 0 
"""
import sys 

a, b = map(int, sys.stdin.readline().rstrip().split())

output = 1 if a <= b else 0 

print(output )