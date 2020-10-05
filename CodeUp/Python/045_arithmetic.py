"""
[ref] https://codeup.kr/problem.php?id=1045

Question:
    1. take two integers; (a, b)
    2. operate +, -, *, quotient, remainder, and dividen
    3. print them 
"""
import sys 

a, b = map(int, sys.stdin.readline().rstrip().split())


print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print("%.2f"  %(a / b))

