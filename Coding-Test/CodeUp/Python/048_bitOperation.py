"""
[ref] https://codeup.kr/problem.php?id=1048

Question:
    1. take two integers; (a, b)
    2. multiply a by 2**b times 
    3. print it out 
"""
import sys 

a, b = map(int, sys.stdin.readline().rstrip().split())


print(a << b)