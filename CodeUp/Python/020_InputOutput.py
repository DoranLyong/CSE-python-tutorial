"""
[ref] https://codeup.kr/problem.php?id=1020

Question:
    1. get your residence numbers; XXXXXX-XXXXXXX
    2. print it in a certain format 
"""

birthday, code = input().split("-")
print("%06d%07d" %(int(birthday), int(code)))