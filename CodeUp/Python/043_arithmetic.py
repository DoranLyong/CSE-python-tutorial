"""
[ref] https://codeup.kr/problem.php?id=1043

Question:
    1. take two integer; (a, b)
    2. get remainder after a/b
"""
import sys 

a, b = map(int, sys.stdin.readline().rstrip().split())

print(a % b)