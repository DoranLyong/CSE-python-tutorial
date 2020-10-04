"""
[ref] https://codeup.kr/problem.php?id=1018

Question:
    1. get the time 
    2. print it in a certain format 
"""
h, m = input().split(':')

print("%d:%d"%(int(h), int(m)))