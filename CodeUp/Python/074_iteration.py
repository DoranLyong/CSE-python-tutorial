# coding=<utf-8>
"""
[ref] https://codeup.kr/problem.php?id=1074

Question: 
    1. get one integer number (1~100) 
    2. count down from it 
"""

num = int(input()) 


num_list = range(num, 0, -1) 


for i in num_list:
    print(i)
