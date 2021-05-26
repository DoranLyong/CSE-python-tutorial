# coding=<utf-8>
"""
[ref] https://codeup.kr/problem.php?id=1073

Question:
    1. print the input if  it is non-zero 
    2. else, break 
"""

l=input().split()

for x in l:
    
    if x!='0':
        print(x)
    else:
        break
