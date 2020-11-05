# coding=<utf-8> 

"""
[ref] https://codeup.kr/problem.php?id=1083

Question: 
    1. get one integer number less than 10; (i.e), 1~9
    2. 369 game 
"""

num = int(input())


if num >= 10: 
    print("input >= 10 ") 
    exit()
    


for i in range(1, num+1): 

    if i%3 == 0: 
        print("X", end = " ")

    else: 
        print(i, end=" ")



