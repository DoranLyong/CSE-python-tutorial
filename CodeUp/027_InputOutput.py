"""
[ref] https://codeup.kr/problem.php?id=1027

Question:
    1. get hour:minute:second
    2. print it in (dd-mm-yyyy) format 
"""

yyyy, mm, dd = input().split(".")

print("%02d-%02d-%04d" %(int(dd), int(mm), int(yyyy)))