"""
[ref] https://codeup.kr/problem.php?id=1046

Question:
    1. take three integers; (a, b, c)
    2. operate sum and average 
    3. print them 
"""
import sys 

a, b, c = map(int, sys.stdin.readline().rstrip().split())

sum = a + b + c 
avg = sum / 3 

print(sum)
print("%.1f" %avg)