"""
[ref] https://codeup.kr/problem.php?id=1062

Question:
    1. take two integers; (x, y) 
    2. operate them with bitwise 'XOR' operation 
    3. print the result in integer 
"""
import sys 

x, y = map(int, sys.stdin.readline().rstrip().split())


output = x ^ y 

print("%d" %output)