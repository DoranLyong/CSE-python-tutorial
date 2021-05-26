# coding=<utf-8>

"""
[ref] https://codeup.kr/problem.php?id=1076 

Question:
    1. get one English letter (a~z) as input 
    2. print the alphabet up to that letter in order. 

"""

data = ord(input()) 


char = ord('a')

while(char <=  data): 
    print(chr(char)) 

    char += 1









"""
https://docs.python.org/ko/3/library/functions.html#ord
https://jaeworld.github.io/2018-11-04/python_ord_chr
"""
