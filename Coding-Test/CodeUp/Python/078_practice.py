# coding=<utf-8>

"""
[ref] https://codeup.kr/problem.php?id=1078i

Question: 
    1. take one integer number (1~100) 
    2. find the sum of even numbers from 1 to that number 
"""


num = int(input())


SUM = 0 


for i in range(1, num+1):

    if i % 2 == 0 :  # if it's even number 
        
        SUM += i 

    else: 
        continue 


print(SUM)


