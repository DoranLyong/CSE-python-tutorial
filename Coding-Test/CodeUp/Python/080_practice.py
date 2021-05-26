# coding=<utf-8> 

"""
[ref] https://codeup.kr/problem.php?id=1080

Question:
    1. get one integer 
    2. keep adding 1,2,3 ... until the sum is larger or equal to the input. 
    3. print the last number for adding 
"""

num = int(input()) 


SUM = 0 
count = 0 

while SUM < num:
    count += 1
    SUM += count 



print(count)
