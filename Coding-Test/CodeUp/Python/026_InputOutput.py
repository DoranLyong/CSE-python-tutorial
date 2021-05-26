"""
[ref] https://codeup.kr/problem.php?id=1026

Question:
    1. get hour:minute:second
    2. print only 'minute' part
"""

h, m, s = input().split(":")

print("%d" %(int(m)))