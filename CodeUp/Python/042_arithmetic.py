"""
[ref] https://codeup.kr/problem.php?id=1042

Question:
    1. take two integer; (a, b)
    2. get quiotient after a/b
"""
import sys 

a, b = map(int, sys.stdin.readline().rstrip().split())

print(a//b)