"""
[ref] https://codeup.kr/problem.php?id=1066

Question:
    1. take three integers; (a, b, c) 
    2. estimate it if even or odd number 
"""
import sys 

a, b, c = map(int, sys.stdin.readline().rstrip().split())


for i in (a, b, c): 
    if i % 2 ==0: 
        print("%s" %"even")

    else:
        print("%s" %"odd")