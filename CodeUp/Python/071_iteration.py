# coding=<utf-8>
"""
[ref] https://codeup.kr/problem.php?id=1071

Question:
    1. receive a seqence integers 
    2. if it is not 0 -> print the input integer 
    3. else -> stop printing 
"""
import sys 

data = list(map(int, sys.stdin.readline().rstrip().split()))


for i in data:
    
    if i != 0: 
        print("%d" %i )

    else:  
        break